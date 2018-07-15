"""
ref:https://github.com/zhedongzheng/finch/blob/master/nlp-models/tensorflow/tf-estimator/only_attn_text_clf_varlen_imdb_test.ipynb

基于IMDB（Internet Movie Database，互联网电影数据库）

用attention进行情感分类（0/1）
"""

import tensorflow as tf
import numpy as np
import sklearn

VOCAB_SIZE = 20000
EMBED_DIM = 50
LOWER_DIM = 5
BATCH_SIZE = 32
LR = {'start': 5e-3, 'end': 5e-4, 'steps': 1500}
N_EPOCH = 2
N_CLASS = 2


def sort_by_len(x, y):
    idx = sorted(range(len(x)), key=lambda i: len(x[i]))
    return x[idx], y[idx]


def pad_sentence_batch(sent_batch):
    max_seq_len = max([len(sent) for sent in sent_batch])
    padded_seqs = [(sent + [0] * (max_seq_len - len(sent))) for sent in sent_batch]
    return padded_seqs


def next_train_batch(X_train, y_train):
    for i in range(0, len(X_train), BATCH_SIZE):
        padded_seqs = pad_sentence_batch(X_train[i: i + BATCH_SIZE])
        yield padded_seqs, y_train[i: i + BATCH_SIZE]


def next_test_batch(X_test):
    for i in range(0, len(X_test), BATCH_SIZE):
        padded_seqs = pad_sentence_batch(X_test[i: i + BATCH_SIZE])
        yield padded_seqs


def train_input_fn(X_train, y_train):
    dataset = tf.data.Dataset.from_generator(
        lambda: next_train_batch(X_train, y_train),
        (tf.int32, tf.int64),
        (tf.TensorShape([None, None]), tf.TensorShape([None])))
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()


def predict_input_fn(X_test):
    dataset = tf.data.Dataset.from_generator(
        lambda: next_test_batch(X_test),
        tf.int32,
        tf.TensorShape([None, None]))
    iterator = dataset.make_one_shot_iterator()
    return iterator.get_next()


def forward(inputs, mode):
    is_training = (mode == tf.estimator.ModeKeys.TRAIN)
    x = tf.contrib.layers.embed_sequence(inputs, VOCAB_SIZE, EMBED_DIM)
    x = tf.layers.dropout(x, 0.2, training=is_training)
    proj = tf.layers.Dense(LOWER_DIM)

    # alignment
    alpha = tf.get_variable('alpha', [LOWER_DIM])
    align = tf.reduce_sum(alpha * tf.nn.relu(proj(x)), axis=-1)

    # masking
    masks = tf.sign(inputs)
    paddings = tf.fill(tf.shape(align), float('-inf'))
    align = tf.where(tf.equal(masks, 0), paddings, align)

    # probability
    align = tf.expand_dims(tf.nn.softmax(align), -1)

    # weighted sum
    x = tf.squeeze(tf.matmul(x, align, transpose_a=True), -1)

    logits = tf.layers.dense(x, N_CLASS)
    return logits


def model_fn(features, labels, mode):
    logits = forward(features, mode)

    if mode == tf.estimator.ModeKeys.PREDICT:
        preds = tf.argmax(logits, -1)
        return tf.estimator.EstimatorSpec(mode, predictions=preds)

    if mode == tf.estimator.ModeKeys.TRAIN:
        global_step = tf.train.get_global_step()

        lr_op = tf.train.exponential_decay(
            LR['start'], global_step, LR['steps'], LR['end'] / LR['start'])

        loss_op = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits=logits, labels=labels))

        train_op = tf.train.AdamOptimizer(lr_op).minimize(
            loss_op, global_step=global_step)

        lth = tf.train.LoggingTensorHook({'lr': lr_op}, every_n_iter=100)

        return tf.estimator.EstimatorSpec(
            mode=mode, loss=loss_op, train_op=train_op, training_hooks=[lth])


(X_train, y_train), (X_test, y_test) = tf.keras.datasets.imdb.load_data(num_words=VOCAB_SIZE)
X_train, y_train = sort_by_len(X_train, y_train)
X_test, y_test = sort_by_len(X_test, y_test)

estimator = tf.estimator.Estimator(model_fn)

for _ in range(N_EPOCH):
    estimator.train(lambda: train_input_fn(X_train, y_train))
    y_pred = np.fromiter(estimator.predict(lambda: predict_input_fn(X_test)), np.int32)
    print("\nValidation Accuracy: %.4f\n" % (y_pred==y_test).mean())