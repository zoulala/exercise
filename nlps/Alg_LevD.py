#-*- coding: utf-8 -*-

'''
Created on 2017��3��22��

@author: zoulingwei
'''
class arithmetic():  
      
    def __init__(self):  
        pass  
    ''''' 【编辑距离算法】 【levenshtein distance】 【字符串相似度算法】 ''' 
    def levenshtein(self,first,second):  
        if len(first) > len(second):  
            first,second = second,first  
        if len(first) == 0:  
            return len(second)  
        if len(second) == 0:  
            return len(first)  
        first_length = len(first) + 1  
        second_length = len(second) + 1  
        distance_matrix = [range(second_length) for x in range(first_length)]   
        #print distance_matrix  
        for i in range(1,first_length):  
            for j in range(1,second_length):  
                deletion = distance_matrix[i-1][j] + 1  
                insertion = distance_matrix[i][j-1] + 1  
                substitution = distance_matrix[i-1][j-1]  
                if first[i-1] != second[j-1]:  
                    substitution += 1  
                distance_matrix[i][j] = min(insertion,deletion,substitution)  
        #print distance_matrix  
        return distance_matrix[first_length-1][second_length-1]  

    ''''' 【向量夹角余弦算法】  【字符串相似度算法】 ''' 
    def cosxy(self, x ,y): #求两个向量的夹角余弦
        if len(x) != len(y):
            return 0
        if max(map(abs,x))==0:
            return 0
        if max(map(abs,y))==0:
            return 0
        fenmu = (sum([i*i for i in x])**0.5) * (sum([j*j for j in y])**0.5)
        fenzi = sum([x[i]*y[i] for i in range(len(x))])
        
        return fenzi/fenmu

    def similar_val(self,val1, val2):
        '''求两个向量相似度（夹角余弦）'''
        len_w = len(val1)
        sum = 0
        sqr1 = 0
        sqr2 = 0
        for i in range(len_w):
            sum += val1[i] * val2[i]
            sqr1 += val1[i] ** 2
            sqr2 += val2[i] ** 2

        result = float(sum) / ((sqr1 ** 0.5) * (sqr2 ** 0.5))

        return result

    def creat_val(self,str1, str2):
        '''两个字符串生成向量空间形式'''
        #u_str1 = str1.decode("utf8")  # 字符串转成Unicode类型
        #u_str2 = str2.decode("utf8")
        u_str1 = str1
        u_str2 = str2
        dic = {}
        for fc in u_str1:
            if fc in dic:
                dic[fc] += 1
            else:
                dic[fc] = 1
        for fc in u_str2:
            if fc in dic:
                dic[fc] += 1
            else:
                dic[fc] = 1
        dic1 = {}
        dic2 = {}
        dic1 = dic1.fromkeys(dic.keys(), 0)
        dic2 = dic2.fromkeys(dic.keys(), 0)

        for fc in u_str1:
            if fc in dic1.keys():
                dic1[fc] += 1
        for fc in u_str2:
            if fc in dic2.keys():
                dic2[fc] += 1
        return dic1.values(), dic2.values()
      
if __name__ == "__main__":  
    arith = arithmetic()  
    print arith.levenshtein('GUMBOsdafsadfdsafsafsadfasfadsfasdfasdfs','GAMBOL00000000000dfasfasfdafsafasfasdfdsa' )
    chax=['中','国']
    chay=['美','国'] 
    
    x=[1,1,1,1,1,1,1]
    y=[1,1,0,0,0,0,0]
    cos = arithmetic()
    print cos.cosxy(x, y)
    
    if chax[0] != chay[0]:
        print chax[0]
    print len(chax)
