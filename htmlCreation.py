#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import sqlite3
import writeHtml
import replace

def htmlCreation (fName):

    dir =  'html/'
    conn = sqlite3.connect('categories.db')
    c = conn.cursor()


    if fName == '0':
        file_name = dir+'root.html'
        f = open(dir + 'root.html', 'w')
        f.write(writeHtml.header)
        f.write("Root")
        f.write(writeHtml.header3)
        f.write(writeHtml.header4)
        c.execute('SELECT * FROM tab_categories WHERE CategoryLevel = 1 ')

        for row in c.fetchall():
            f.write(str(row) + '<p>')

        f.write(writeHtml.footer2)
        f.write(writeHtml.header4)
        c.execute('SELECT * FROM tab_categories WHERE CategoryLevel = 2 ')

        for row in c.fetchall():
            f.write(str(row) + '<p>')
        f.write(writeHtml.footer2)
        f.write(writeHtml.header4)
        c.execute('SELECT * FROM tab_categories WHERE CategoryLevel = -1 ')

        for row in c.fetchall():
            f.write(str(row) + '<p>')
    else:
        file_name = dir + fName + '.html'
        f = open(dir + fName + '.html', 'w')
        f.write(writeHtml.header)
        f.write(fName)
        f.write(writeHtml.header2)
        c.execute('SELECT CategoryID,CategoryLevel,CategoryName,CategoryParentID FROM tab_categories WHERE CategoryParentID = '+ fName )
        for row in c.fetchall():
            if row == None:
                f.write("No info related whit this ID")
            else:
                f.write(str(row) + '<p>')

    f.write(writeHtml.footer)
    f.close()
    replace.replaceHtml1(file_name)
    replace.replaceHtml2(file_name)
    replace.replaceHtml3(file_name)
    replace.replaceHtml4(file_name)
    replace.replaceHtml5(file_name)
