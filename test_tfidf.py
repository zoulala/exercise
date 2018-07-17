from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer




X_test = [u'没有好1 地方 都是 他乡',u'没有 你 的 旅行 都是 流浪']
# count_vec = TfidfVectorizer(ngram_range=(1,1),min_df=0, max_df=0.9,use_idf=1,smooth_idf=1, sublinear_tf=1, token_pattern=r"(?u)\w")
count_vec=CountVectorizer(token_pattern=r"(?u)\w")  # 设置正则匹配规则，token_pattern=r"(?u)\b\w\w+\b"以空格间隔匹配
print (count_vec.fit_transform(X_test).toarray())
print (count_vec.fit_transform(X_test))
print ('\nvocabulary list:\n')
for key,value in count_vec.vocabulary_.items():
    print (key,value)