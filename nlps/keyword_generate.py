
from lib import nlp_jieba

def gen_keywords(titleslist):
    segob = nlp_jieba.Nlp_Jieba()
    user_keys = {}
    for t in titleslist:
        tcut = segob.word_segment(t)
        for tw in tcut:
            if tw in user_keys and len(tw) > 1:
                user_keys[tw] += 1
            elif tw not in user_keys and len(tw) > 1:
                user_keys[tw] = 1

    with open('trains/model/userkey1.txt', 'w', encoding='utf8') as kf:
        for w in user_keys:
            kf.write(w + ' %d\n' % user_keys[w])

def gen_keywords2(stop_words, titleslist):
    '''jieba关键词生成'''
    stop_words.sort(key=len,reverse=True)

    segob = nlp_jieba.Nlp_Jieba()
    keyslist = []
    for t in titleslist:

        tcut = segob.jieba_tf_idf(t)

        k = 0
        if len(tcut) == 0:
            keyslist.append(t)
        for w in tcut:
            if k>1:  # 限制每个句子最多两个有效关键词
                break
            if w[0] not in stop_words:  # 这里开始去停用词，不让停用词作为关键词（增加了人工关键词时，最好不用）
                keyslist.append(w[0])
                k += 1
    keyslist = list(set(keyslist))

    with open('trains/model/userkey2.txt', 'w', encoding='utf8') as kf:
        for w in keyslist:
            kf.write(w + '\n')
    return keyslist



if __name__ == "__main__":




    str = '酒是什么'
    str = str.replace('什么','')

    keyclass = nlp_jieba.Nlp_Jieba()

    keys1 = keyclass.jieba_textrank(str)
    keys2 = keyclass.jieba_tf_idf(str)

    print (keys1)
    print (keys2)
