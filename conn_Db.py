#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
from xml.dom import minidom
import sqlite3
def conn_db(name_file):
    file = name_file
    conn = sqlite3.connect('categories.db')
    c = conn.cursor()

    # Define the functions

    def drop_table(): #drop a table
        c.execute('DROP TABLE tab_categories;')

    def create_table():  # Function to create the DataBase
        c.execute(
            'CREATE TABLE IF NOT EXISTS tab_categories(CategoryID TEXT,CategoryLevel TEXT,CategoryName TEXT,CategoryParentID TEXT)')

    def data_entry(CategoryID, CategoryLevel, CategoryName, CategoryParentID):  # Function to send the data to the Data Base
        c.execute('INSERT INTO tab_categories (CategoryID,CategoryLevel,CategoryName,CategoryParentID)VALUES (?,?,?,?)',
                 (CategoryID, CategoryLevel, CategoryName, CategoryParentID))

    # Parce the document XML
    doc = minidom.parse(name_file)
    #Drop and create the table again
    drop_table
    create_table()
    staffs = doc.getElementsByTagName("Category")
    for staff in staffs:
        CategoryID = staff.getElementsByTagName("CategoryID")[0]
        CategoryLevel = staff.getElementsByTagName("CategoryLevel")[0]
        CategoryName = staff.getElementsByTagName("CategoryName")[0]
        CategoryParentID = staff.getElementsByTagName("CategoryParentID")[0]
        #print("CategoryID:%s, CategoryName:%s, CategoryParentID:%s" %
              #(CategoryID.firstChild.data,
              #CategoryLevel.firstChild.data,
              #CategoryName.firstChild.data))

        data_entry(CategoryID.firstChild.data,
                   CategoryLevel.firstChild.data,
                   CategoryName.firstChild.data,
                   CategoryParentID.firstChild.data)

        conn.commit()

    c.close()
    conn.close()

