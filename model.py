#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo

#DBimports
import sqlite3

#Model

def drop_table(): #Function to drop a table
    #vars
    file = "db/categories.db"
    #vars db
    connection = sqlite3.connect(file)
    cursor = connection.cursor()

    #statement executes
    cursor.execute('DROP TABLE IF EXISTS tab_categories;')
    #close
    connection.close()


def create_table():  # Function to create the DataBase
    # vars DB
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()
    # statement executes
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS tab_categories(CategoryID TEXT,CategoryLevel TEXT,CategoryName TEXT,CategoryParentID TEXT)')
    # close
    connection.close()


def insert_table(category_ID, category_Level, category_Name, category_Parent_ID):  # Function to send the data to the Data Base
    #vars DB
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()
    # statement executes
    cursor.execute('INSERT INTO tab_categories (CategoryID,CategoryLevel,CategoryName, CategoryParentID)VALUES (?,?,?,?)',
                        (category_ID, category_Level, category_Name, category_Parent_ID))
    connection.commit()
    print(category_ID + ' - ' + category_Name + ' Inserted ')
    #close
    connection.close()

#This is the previous model


'''
def create_table():  # Function to create the DataBase
    # vars DB
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()
    # statement executes
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS tab_categories(CategoryID TEXT,CategoryLevel TEXT,CategoryName TEXT,CategoryParentID TEXT)')
    # close
    connection.close()

def insert_table(category_ID, category_Level, category_Name, category_Parent_ID):  # Function to send the data to the Data Base
    #vars DB
    connection = sqlite3.connect('db/categories.db')
    cursor = connection.cursor()
    # statement executes
    cursor.execute('INSERT INTO tab_categories (CategoryID,CategoryLevel,CategoryName,CategoryParentID)VALUES (?,?,?,?)',
                        (category_ID, category_Level, category_Name, category_Parent_ID))
    connection.commit()
    #close
    connection.close()
'''