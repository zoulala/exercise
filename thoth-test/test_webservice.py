#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# *****************************************************
#
# file:     test_webservice.py
# author:   zlw2008ok@126.com
# date:     2022/12/8
# desc:     http://www.yyt009.com/buildIntroduction.html
#
# cmd>e.g.:  
# *****************************************************

# from suds.client import Client
#
# url = 'http://8.142.161.142/webserviceHHKB2/HHKB2.dll'
# url = "http://8.142.161.142/webserviceHHKB2/HHKB2.dll/wsdl/IHhkbWebService"
#
# client = Client(url)
# print(client)

import base64
from suds import client
url = "http://8.142.161.142/webserviceHHKB2/HHKB2.dll/wsdl/IHhkbWebService"

'''
 	
IHhkbWebService [WSDL]
ws_hhkb_GetVer
ws_hhkb_GetCount
ws_hhkb_GetList
ws_hhkb_GetDrugList
ws_hhkb_GetDetail
ws_hhkb_GetGroup
ws_hhkb_GetTreatDiseases
ws_hhkb_GetDrugPicture
 	
IWSDLPublish [WSDL]
 	Lists all the PortTypes published by this Service
GetPortTypeList
GetWSDLForPortType
GetTypeSystemsList
GetXSDForTypeSystem

IHhkbWebService [WSDL]  (urn:HhkbWebServiceIntf-IHhkbWebService)
 	string	ws_hhkb_GetVer(int iBH)
 	int	ws_hhkb_GetCount(int iKindBH)
 	string	ws_hhkb_GetList(int iKindBH, int iBegin, int iEnd)
 	string	ws_hhkb_GetDrugList(int iBegin, int iEnd)
 	string	ws_hhkb_GetDetail(int iKindBH, string strKBBM)
 	string	ws_hhkb_GetGroup(int iGroupBH, string strKBBM)
 	string	ws_hhkb_GetTreatDiseases(string strKBBM)
 	string	ws_hhkb_GetDrugPicture(string strKBBM)
'''

web_s = client.Client(url)
# print(web_s)
res1 = web_s.service.ws_hhkb_GetCount(11)
print(res1)

res2 = web_s.service.ws_hhkb_GetList(11,1,3)
res2 = base64.b64decode(res2).decode("gbk")
print(res2)

