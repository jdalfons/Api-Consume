#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import sqlite3
import writeHtml
import replace

def htmlCreation (fName):

    #vars
    dir =  'html/'
    #vars DB
    connection = sqlite3.connect('db/categories.db')
    cursor_val1 = connection.cursor()
    cursor_val2 = connection.cursor()

    #Creation of the Directory
    file_name = dir + fName + '.html'
    file = open(dir + fName + '.html', 'w')
    file.write(writeHtml.header)
    file.write(fName)
    file.write(writeHtml.header2)

    # Create the data structure function
    def get_child(category):
        sql = 'SELECT * FROM tab_categories WHERE CategoryParentID = ' + category
        cursor_val1.execute(sql)
        for row in cursor_val1.fetchall():
            file.write('["' + row[1] + '"-"' + row[0] + '"-"' + row[2] + '"-"' + row[3] + '"]')
            get_child(row[0])

    # This is the function that recives the pathern
    cursor_val1.execute('SELECT * FROM tab_categories WHERE CategoryID = 99')
    row = cursor_val1.fetchall()
    value = row[0]
    file.write('["' + value[1] + '"-"' + value[0] + '"-"' + value[2] + '"-"' + value[3] + '"]')
    count_level = 5 - int(value[1])
    cursor_val2.execute('SELECT * FROM tab_categories WHERE CategoryParentID = 99')
    for row in cursor_val2.fetchall():
        file.write('["' + row[1] + '"-"' + row[0] + '"-"' + row[2] + '"-"' + row[3] + '"]')
        get_child(row[0])

    file.write(writeHtml.footer)
    file.close()
    replace.replaceHtml1(file_name)
    replace.replaceHtml2(file_name)
    replace.replaceHtml3(file_name)
    #replace.replaceHtml4(file_name)
    #replace.replaceHtml5(file_name)
