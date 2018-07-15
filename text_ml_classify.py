"""
提取文本tfIDF特征数据
用多种分类算法对文本数据进行分类（多类）
"""


import pandas as pd, numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import svm,tree,linear_model

flag = 0  # 迭代器读取数据，
# flag = 1  # 全部读取数据到内存，

if flag == 0:

    train_filename = "train_set.csv"
    with open(train_filename,'r',encoding="utf8") as f:
        line = f.readline()
        line = f.readline()
        i = 0
        train_x = []
        train_y = []
        val_x = []
        val_y = []
        while line:
            if i<10000:
                line_list = line.strip().split(',')
                assert len(line_list)==4 ," len(line_list) not is 4"
                train_x.append(line_list[2])
                train_y.append(int(line_list[3])-1)
                line = f.readline()
            elif i<20000:
                line_list = line.strip().split(',')
                assert len(line_list)==4 ," len(line_list) not is 4"
                val_x.append(line_list[2])
                val_y.append(int(line_list[3])-1)
                line = f.readline()
            else:
                break
            i += 1


    test_filename = "test_set.csv"
    with open(test_filename,'r',encoding="utf8") as f:
        line = f.readline()
        line = f.readline()
        i = 0
        test_x = []
        test_y = []
        while line:
            line_list = line.strip().split(',')
            assert len(line_list)==3 ," len(line_list) not is 4"
            test_x.append(line_list[2])
            line = f.readline()
            i += 1
            if i>10000:
                break
    print('data read finished.')

if flag == 1:
    column = "word_seg"
    train = pd.read_csv('train_set.csv')
    test = pd.read_csv('test_set.csv')
    test_id = test["id"].copy()

    y = (train["class"]-1).astype(int)
    train_x = train[column][:-10000]
    train_y = y[:-10000]
    val_x =  train[column][-10000:]
    val_y = y[-10000:]
    test_x = test[column]
    print('data read finished.')


vec = TfidfVectorizer(ngram_range=(1,2),min_df=3, max_df=0.9,use_idf=1,smooth_idf=1, sublinear_tf=1)
trn_term_doc = vec.fit_transform(train_x)
val_term_doc = vec.transform(val_x)
test_term_doc = vec.transform(test_x)
fid0=open('baseline.csv','w')

##  -------------- SVM -------------
lin_clf = svm.LinearSVC()

## ------------ DT -----------
# lin_clf = tree.DecisionTreeClassifier(min_samples_split=4)  # 最小样本分割，越小树的深度越深，越容易过拟合

## ------------- LR ----------
# lin_clf = linear_model.LogisticRegression()


lin_clf.fit(trn_term_doc,train_y)
val_pre = lin_clf.predict(val_term_doc)
print("val accuracy score:",(val_pre==val_y).mean())



preds = lin_clf.predict(test_term_doc)
i=0
fid0.write("id,class"+"\n")
for item in preds:
    fid0.write(str(i)+","+str(item+1)+"\n")
    i=i+1
fid0.close()