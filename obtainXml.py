#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import requests
import replace
import conn_Db

#Create the function to consume the Api and obtain the categories
def obtainXml():

    categories = ['20081', '550', '2984', '267', '12576', '625', '15032', '11450', '11116', '1', '58058', '293',
                  '14339', '237', '11232', '45100', '172008', '26395', '11700', '281', '11233', '619',
                  '1281', '870', '10542', '316', '888', '64482', '260', '1305', '220', '3252', '1249', '99']
    path = 'Categories/'
    #URL this URL is from the SandBox of Api
    for x in range (0, 34):
        name_file = path +'categories' + categories[x] +'.xml'
        file = open(name_file, 'wb')
        url = 'http://open.api.sandbox.ebay.com/Shopping?callname=GetCategoryInfo&appid=EchoBay62-5538-466c-b43b-662768d6841&version=967&siteid=0&CategoryID='+ categories[x] + '&IncludeSelector=ChildCategories'
        response = requests.get(url)
        print (str(x) + ' - ' +  url)
        file.write(response.content)#We create the file and write the XML
        file.close()
        replace.replaceAmp(name_file)
        replace.replaceComma(name_file)
        conn_Db.conn_db(name_file)

