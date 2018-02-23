#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import requests
import replace
import os
import model

#DBimports

from xml.dom import minidom
import sqlite3


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