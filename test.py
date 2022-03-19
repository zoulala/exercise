#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test.py
# author:   zoulingwei@zuoshouyisheng.com
# date:     2020-02-12
# brief:    
#
# cmd>e.g:  
# *****************************************************


import xlrd
import re




file = '紧急程度症状属性.xlsx'

# xlbook = xlrd.open_workbook(file)
# sh = xlbook.sheet_by_index(0)
# n = sh.nrows
# m = sh.ncols
#
#
# sf = open('symptom_degree.dict','w')
#
# for i in range(1,n):
#    raw = sh.row_values(i)
#    # sym,attr,schema,attr_value,keyword,factor,scope,level,feedback,_ = raw
#
#    print('\t'.join(raw[:-1]).replace('\n',''))
#    sf.write('\t'.join(raw[:-1]).replace('\n','')+'\n')
# sf.close()

# symptom_level_dict = {}
# with open('symptom_degree.dict','r') as f:
#     for line in f:
#         line = line.strip('\n')
#         data = line.split('\t')
#         if len(data) != 9:continue
#         sym, attr, schema, attr_value, keyword, factor, scope, level, feedback = data
#
#         if not attr:
#             symptom_level_dict[sym] = {'level': level, 'feedback': feedback}
#         elif sym not in symptom_level_dict:
#             symptom_level_dict[sym] = {'attrs':{attr:{attr_value:{'level':level,'feedback':feedback}}}}
#         else:
#             if attr not in symptom_level_dict[sym]['attrs']:
#                 symptom_level_dict[sym]['attrs'][attr] = {attr_value:{'level':level,'feedback':feedback}}
#             else:
#                 symptom_level_dict[sym]['attrs'][attr][attr_value] = {'level': level, 'feedback': feedback}
#

#
# with open('symptom_degree.dict','r') as f:
#     for line in f:
#         line = line.strip('\n')
#         data = line.split('\t')
#         if len(data) != 9:continue
#         symptom, attr, schema, attr_value, keyword, factor, scope, level, feedback = data
#         if schema in ['temperature','blood_pressure']:
#             key = '_'.join([term for term in [schema,attr_value] if term])
#         else:
#             key = '_'.join([term for term in [symptom,schema,attr_value] if term])
#
#         if key not in symptom_level_dict:
#             symptom_level_dict[key] = (level,feedback)
#
#
#
# print(symptom_level_dict)



def read_symptom_level_dict(filename):
    symptom_level_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.decode('utf8').strip('\n')
            data = line.split('\t')
            if len(data) != 9: continue
            symptom, attr, schema, attr_value, keyword, factor, scope, level, feedback = data
            if schema in ['temperature', 'blood_pressure']:
                key = '_'.join([term for term in [schema, attr_value] if term])
            else:
                key = '_'.join([term for term in [symptom, schema, attr_value] if term])

            if key not in symptom_level_dict:
                symptom_level_dict[key] = (level,feedback)
    return symptom_level_dict


def get_symptom_level(symptom, attr='', attr_value='', symptom_level_dict={}):
    '''
        attr 可以是空
        attr_value 可以是空
        0-普通
        1-严重
        2-紧急
    '''

    level_dict = {u'紧急':2,u'严重':1,u'普通':0}

    def num_convertor(attr, attr_value):
        if attr == 'temperature':
            try:
                num = float(attr_value)
                if num>=41:
                    return u'超高热'
                elif num>=39:
                    return u'高热'
                else:
                    return u'无'
            except:
                return u'未知'

        if attr == 'blood_pressure':
            vas = attr_value.split('_')
            if len(vas) !=2:return u'未知'
            num = re.findall(r'^\d+', vas[1])
            if num:
                num = int(num[0])
            else:
                return u'未知'

            if vas[0] ==u'高压':
                if num>=180:
                    return u'过高'
                elif num<90:
                    return u'过低'
                else:
                    return u'无'
            if vas[0] == u'低压':
                if num >= 110:
                    return u'过高'
                elif num < 60:
                    return u'过低'
                else:
                    return u'无'
        return u'未知'

    level1, feedback1 = symptom_level_dict.get(symptom, (u'普通', ''))

    if attr in ['temperature','blood_pressure']:
        attr_value = num_convertor(attr, attr_value)
        key = '_'.join([term for term in [attr, attr_value] if term])
        level2,feedback2 = symptom_level_dict.get(key,(u'普通',''))
    else:
        key = '_'.join([term for term in [symptom, attr, attr_value] if term])
        level2,feedback2 = symptom_level_dict.get(key, (u'普通',''))

    # level_code = max(level_dict[level1],level_dict[level2])
    if level_dict[level1] > level_dict[level2]:
        level = level1
        level_code = level_dict[level1]
        feedback = feedback1
    else:
        level = level2
        level_code = level_dict[level2]
        feedback = feedback2

    return level,level_code,feedback


symptom_level_dict = read_symptom_level_dict('symptom_degree.dict')

level,level_code,feedback=get_symptom_level(u'头晕','','',symptom_level_dict)

print level,level_code,feedback

exit()
with open('attr.data','r') as f:
    for line in f:
        line = line.strip().decode('utf8')
        if not line:continue
        data = line.split('\t')

        if len(data)==1:
            symptom = data[0]
        if len(data)==2:
            symptom,attr = data
        if len(data)==3:
            symptom,attr,attr_value = data

        level,level_code,feedback=get_symptom_level(symptom,attr,attr_value,symptom_level_dict)
        print line
        print level,level_code,feedback


