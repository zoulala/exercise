import pkuseg
import jieba


text = "左肺下叶基底段胸膜下见不规则结节影，边界欠光整，范围约1.7*1.8cm，增强扫描明显强化；左肺斜裂旁见小结节影，径约0.4cm。右肺中叶及左肺上叶舌段见高密度索条影，边界欠清。纵隔内及双肺门见多个淋巴结影，部分伴钙化，短径均小于1.0cm。左肺下叶胸膜增厚、钙化；双侧胸腔未见积液。扫及多个胸腰椎、胸骨、双侧部分肋骨及右侧肩胛骨见骨质破坏影"

# 示例1：使用默认配置进行分词（如果用户无法确定分词领域，推荐使用默认模型分词）
seg = pkuseg.pkuseg()
result = seg.cut(text)
print(result)

# 示例2：细领域分词（如果用户明确分词领域，推荐使用细领域模型分词）

seg = pkuseg.pkuseg(model_name='medicine')  # 程序会自动下载所对应的细领域模型
result = seg.cut(text)
print(result)


# jieba 对比
cut_words = jieba.cut(text, HMM=False)
words = []
for word in cut_words:
    words.append(word)
print(words)

