
def gen_new_questions(query_answers):
    """从众多问答对中提取新问答，并入库"""

    # 统计问答对关键词频数，排序
    keys_dict = {}
    querys = query_answers.titles
    for title in querys:
        key = gen_keywords(title)
        keys_dict[key] += 1

    # 选择排序靠前的关键词所涉及的q&a对作为候选问答对


    # 选择排序靠前的关键词所涉及的库中原q&a对作为筛选时问题集

    # 通过计算候选问答对中每条与原问题集的相似度，如果最高相似度<阈值，则入库（保证入库前的问答对之间的相似度都>阈值），否则说明库中存在类似问题