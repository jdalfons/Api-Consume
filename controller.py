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
    #Create the variables header and xml to sent in the POST method, I

    ############# If you download the repository insert the api user credentials#############
    headers = {"X-EBAY-API-CALL-NAME": "GetCategories",
               "X-EBAY-API-APP-NAME": "", ##### Put your ebay app name
               "X-EBAY-API-CERT-NAME": "", ##### put your ebay cert
               "X-EBAY-API-DEV-NAME": "", ##### put your ebay api dev name
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

    #Send the request with the headers and the XML
    rsp = requests.post(url, headers=headers, data=xml).text

    #Print the XML with the response
    #print ('XML created')

    #Here we read the XML of the response.
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


#Define the function -- This function read the XML and  go through the required tags to insert to the DB
def insert_categories(file):
    #Vars
    #doc = minidom.parse('Categories/category_1/category_root.xml')
    file_cat = minidom.parse(file)
    staffs = file_cat.getElementsByTagName("Category")

    #connection vars
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()


    #For to go through all the tags of the archive an insert the info in the archive to the DB with the function  insert_table
    for staff in staffs:
        category_ID = staff.getElementsByTagName("CategoryID")[0]
        category_Level = staff.getElementsByTagName("CategoryLevel")[0]
        category_Name = staff.getElementsByTagName("CategoryName")[0]
        category_Parent_ID = staff.getElementsByTagName("CategoryParentID")[0]
        #Insert in the table with the function insert_table
        model.insert_table(category_ID.firstChild.data,
                     category_Level.firstChild.data,
                     category_Name.firstChild.data,
                     category_Parent_ID.firstChild.data)
