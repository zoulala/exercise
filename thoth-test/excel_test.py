#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     excel_test.py
# author:   zlw2008ok@126.com
# date:     2023/7/25
# desc:     excel增加颜色
#
# cmd>e.g.:  
# *****************************************************

import config
from libs.med_parser import SlotFill,MkgParser

import xlrd,xlwt

def slot_val():

    workbook2 = xlwt.Workbook()
    sheet2 = workbook2.add_sheet("1")

    row_idx = 0
    n = 500


    with open('zhusu.txt','r') as f:
        for line in f:
            print(row_idx)
            if row_idx > n:
                break
            line = line.strip()
            if not line:continue
            js_out = sl.request(line)
            tags = js_out.get('tags',[])

            offset_list = []
            for _dic in tags:
                offset1 = _dic.get('offset')
                offset2 = offset1+_dic.get('length')
                type = _dic.get('tag_type')
                if type=='SYMPTOM':
                    offset_list.append([offset1,offset2,'sym'])
                if type =='DISEASE':
                    offset_list.append([offset1, offset2, 'dis'])
                if type =='DRUG':
                    offset_list.append([offset1, offset2, 'drg'])

            row_idx += 1
            sheet2.write(row_idx, 0, line)
            offset_list.sort(key=lambda _x: _x[0])
            offset = 0
            rich_text = []
            for offset_info in offset_list:
                if offset_info[0] >=offset:
                    rich_text.append(line[offset:offset_info[0]])
                    if offset_info[2] == 'dis':
                        red_font = xlwt.easyfont('color_index red')
                    elif offset_info[2] == 'sym':
                        red_font = xlwt.easyfont('color_index blue')
                    elif offset_info[2] == 'drg':
                        red_font = xlwt.easyfont('color_index green')
                    rich_text.append((line[offset_info[0]:offset_info[1]], red_font))
                    offset = offset_info[1]

            rich_text.append(line[offset:])
            sheet2.write_rich_text(row_idx, 1, rich_text)

    workbook2.save("slotfilling_eval.xls")


def mkg_val():
    workbook2 = xlwt.Workbook()
    sheet2 = workbook2.add_sheet("1")

    row_idx = 0
    n = 500
    offset_list=[]
    with open('zhusu.txt', 'r') as f:
        for line in f:
            print(row_idx)
            if row_idx > n:
                break
            line = line.strip()
            if not line: continue
            mkg_rst = mkg.request(line)
            doc_rst = mkg_rst.get('Doc_Rst', [])

            ne_rows = []
            for a_type in doc_rst:
                ne_type = a_type.get('ne_type', '')
                type_name = a_type.get('name', '')
                ne_list = a_type.get('ne_list', [])

                # nes = [a_ne['NAME'] for a_ne in ne_list]
                nes = []
                for a_ne in ne_list:
                    ne_name = a_ne['NAME']
                    ne_offset = a_ne['OFFSET']
                    props = a_ne.get('PROPERTY')

                    # for pro in props:
                    #     p_name = pro.get('NAME')
                    #     p_offset = pro.get('OFFSET', [])
                    #     p_offset_list.extend(p_offset)
                    if 'SYMPTOM' in ne_type:
                        for offs in ne_offset:
                            offs.append('sym')
                        offset_list.extend(ne_offset)
                    if 'DISEASE' in ne_type:
                        for offs in ne_offset:
                            offs.append('dis')
                        offset_list.extend(ne_offset)
                    if 'DRUG' in ne_type:
                        for offs in ne_offset:
                            offs.append('drg')
                        offset_list.extend(ne_offset)

            # for off in offset_list:
            #     off.append(1)

            # for off in p_offset_list:
            #     off.append(2)

            row_idx += 1
            sheet2.write(row_idx, 0, line)
            offset_list.sort(key=lambda _x: _x[0])
            offset = 0
            rich_text = []
            for offset_info in offset_list:
                if offset_info[0] >=offset:
                    rich_text.append(line[offset:offset_info[0]])
                    if offset_info[2] == 'dis':
                        red_font = xlwt.easyfont('color_index red')
                    elif offset_info[2] == 'sym':
                        red_font = xlwt.easyfont('color_index blue')
                    elif offset_info[2] == 'drg':
                        red_font = xlwt.easyfont('color_index green')
                    rich_text.append((line[offset_info[0]:offset_info[1]], red_font))
                    offset = offset_info[1]

            rich_text.append(line[offset:])
            sheet2.write_rich_text(row_idx, 1, rich_text)

    workbook2.save("mkg_eval.xls")

# slot_val()
mkg_val()