#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo

import requests
import replace
import model

#DBimports
from xml.dom import minidom
import sqlite3


def obtainXmlandcreatetable():
    url = 'https://api.sandbox.ebay.com/ws/api.dll'
    #Create the variables header and xml to sent in the POST method
    headers = {"X-EBAY-API-CALL-NAME": "GetCategories",
               "X-EBAY-API-APP-NAME": "EchoBay62-5538-466c-b43b-662768d6841",
               "X-EBAY-API-CERT-NAME": "00dd08ab-2082-4e3c-9518-5f4298f296db",
               "X-EBAY-API-DEV-NAME": "16a26b1b-26cf-442d-906d-597b60c41c19",
               "X-EBAY-API-SITEID": "0",
               "X-EBAY-API-COMPATIBILITY-LEVEL": "861"}

    xml = """<?xml version="1.0" encoding="utf-8"?>
            <GetCategoriesRequest xmlns="urn:ebay:apis:eBLBaseComponents">
            <RequesterCredentials>
            <eBayAuthToken>AgAAAA**AQAAAA**aAAAAA**PlLuWA**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4GlDpaDpAudj6x9nY+seQ**LyoEAA**AAMAAA**wSd/jBCbxJHbYuIfP4ESyC0mHG2Tn4O3v6rO2zmnoVSF614aVDFfLSCkJ5b9wg9nD7rkDzQayiqvwdWeoJkqEpNQx6wjbVQ1pjiIaWdrYRq+dXxxGHlyVd+LqL1oPp/T9PxgaVAuxFXlVMh6wSyoAMRySI6QUzalepa82jSQ/qDaurz40/EIhu6+sizj0mCgjcdamKhp1Jk3Hqmv8FXFnXouQ9Vr0Qt+D1POIFbfEg9ykH1/I2CYkZBMIG+k6Pf00/UujbQdne6HUAu6CSj9wGsqQSAEPIXXvEnVmtU+6U991ZUhPuA/DMFEfVlibvNLBA7Shslp2oTy2T0wlpJN+f/Jle3gurHLIPc6EkEmckEpmSpFEyuBKz+ix4Cf4wYbcUk/Gr3kGdSi20XQGu/ZnJ7Clz4vVak9iJjN99j8lwA2zKW+CBRuHBjZdaUiDctSaADHwfz/x+09bIU9icgpzuOuKooMM5STbt+yJlJZdE3SRZHwilC4dToTQeVhAXA4tFZcDrZFzBmJsoRsJYrCdkJBPeGBub+fqomQYyKt1J0LAQ5Y0FQxLHBIp0cRZTPAuL/MNxQ/UXcxQTXjoCSdZd7B55f0UapU3EsqetEFvIMPxCPJ63YahVprODDva9Kz/Htm3piKyWzuCXfeu3siJvHuOVyx7Q4wyHrIyiJDNz5b9ABAKKauxDP32uqD7jqDzsVLH11/imKLLdl0U5PN+FP30XAQGBAFkHf+pAvOFLrdDTSjT3oQhFRzRPzLWkFg</eBayAuthToken>
            </RequesterCredentials>
            <CategorySiteID>0</CategorySiteID>
            <DetailLevel>ReturnAll</DetailLevel>
            </GetCategoriesRequest>"""

    rsp = requests.post(url, headers=headers, data=xml).text

    print ('XML created')


    path = 'Categories/'
    name_file = path + 'category_root.xml'
    #file manage
    file = open(name_file, 'wb')
    file.write(rsp.encode())
    file.close()

    #Replace special characters
    replace.replaceAmp(name_file)
    replace.replaceComma(name_file)

    insert_categories(name_file)


def insert_categories(file):
    #Vars
    #doc = minidom.parse('Categories/category_1/category_root.xml')
    file_cat = minidom.parse(file)
    staffs = file_cat.getElementsByTagName("Category")

    #connection vars
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()


    #For to control the info in the archive
    for staff in staffs:
        category_ID = staff.getElementsByTagName("CategoryID")[0]
        category_Level = staff.getElementsByTagName("CategoryLevel")[0]
        category_Name = staff.getElementsByTagName("CategoryName")[0]
        category_Parent_ID = staff.getElementsByTagName("CategoryParentID")[0]
        BestOffer_Enabled = staff.getElementsByTagName("BestOfferEnabled"[0])
        #Insert in the table with the model
        model.insert_table(category_ID.firstChild.data,
                     category_Level.firstChild.data,
                     category_Name.firstChild.data,
                     category_Parent_ID.firstChild.data)

#This is the previous controller

'''
#We obtain the root category with this function
def obtain_Roots():

    #Vars
    url = 'http://open.api.sandbox.ebay.com/Shopping?callname=GetCategoryInfo&appid=EchoBay62-5538-466c-b43b-662768d6841&version=967&siteid=0&CategoryID=-1&IncludeSelector=ChildCategories'
    response = requests.get(url)
    path = 'Categories/'
    name_file = path + 'category_root.xml'

    if not os.path.exists(path):
        os.makedirs(path)

    #file manage
    file = open(name_file, 'wb')
    file.write(response.content)
    file.close()

    #Replace special characters
    replace.replaceAmp(name_file)
    replace.replaceComma(name_file)
    insert_categories(name_file)


#We can obtain other categoryes with this function
def obtain_categories(category , range):
    # Vars

    url = 'http://open.api.sandbox.ebay.com/Shopping?callname=GetCategoryInfo&appid=EchoBay62-5538-466c-b43b-662768d6841&version=967&siteid=0&CategoryID='+ category +'&IncludeSelector=ChildCategories'
    response = requests.get(url)
    path = 'Categories/category_'+ range +'/'
    name_file = path + 'category_'+category+'.xml'
    validation =  name_file

    if not os.path.exists(path):
        os.makedirs(path)

    #if not os.path.exists(validation):

    # file manage
    file = open(name_file, 'wb')
    file.write(response.content)
    file.close()
    #print(category)

    # Replace special characters
    replace.replaceAmp(name_file)
    replace.replaceComma(name_file)
    insert_categories(name_file)
    #else:
       #print('This xml exist ' + category)



#With this function we can insert the category
def insert_categories(file):
    #Vars
    #doc = minidom.parse('Categories/category_1/category_root.xml')
    file_cat = minidom.parse(file)
    staffs = file_cat.getElementsByTagName("Category")

    #connection vars
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()


    #For to control the info in the archive
    for staff in staffs:
        category_ID = staff.getElementsByTagName("CategoryID")[0]
        category_Level = staff.getElementsByTagName("CategoryLevel")[0]
        category_Name = staff.getElementsByTagName("CategoryName")[0]
        category_Parent_ID = staff.getElementsByTagName("CategoryParentID")[0]

        #Insert in the table with the model
        model.insert_table(category_ID.firstChild.data,
                     category_Level.firstChild.data,
                     category_Name.firstChild.data,
                     category_Parent_ID.firstChild.data)


#Controller
#Controller to create all the categories

def controller_categories():
    #Vars
    file = 'Categories/category_1/category_root.xml'
    #connection vars
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()
    #selectstatement
    for x in range (1, 5):
        num_cat = (str(x))
        cursor.execute('SELECT * FROM tab_categories WHERE CategoryLevel = ' + num_cat)
        for row in cursor.fetchall():
            print(row[0] + ' - ' + str(x))
            obtain_categories(row[0], str(x))

'''