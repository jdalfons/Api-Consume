#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo

def replaceAmp(fname):
    textToFind = '&amp;'
    textToReplace = 'and'
    file = fname

    inputfile = file
    with open(inputfile,'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind,textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceTag(fname):
    textToFind = '<?xml version="1.0" encoding="UTF-8"?>'
    textToReplace = ''
    file = fname

    inputfile = file
    with open(inputfile,'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind,textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceComma(fname):
    textToFind = ','
    textToReplace = ''
    file = fname

    inputfile = file
    with open(inputfile,'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind,textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceHtml1(fname):

    list = ['<tr><td>0',
            '<tr class="active"><td>1',
            '<tr class="danger"><td>2',
            '<tr class="success"><td>3',
            '<tr class="info"><td>4',
            '<tr class="warning"><td>5',
            '<tr><td>6',
            '<tr><td>7']

    for x in range (1 , 7):
        textToFind = '["' + str(x)
        textToReplace = list[x]
        file = fname

        inputfile = file
        with open(inputfile, 'r') as inputfile:
            fileData = inputfile.read()
            freq = 0
            freq = fileData.count(textToFind)
        destibnationpath = file
        fileData = fileData.replace(textToFind, textToReplace)
        with open(destibnationpath, 'w') as file:
            file.write(fileData)

def replaceHtml2(fname):
    textToFind = '"-"'
    textToReplace = "</td><td>"
    file = fname

    inputfile = file
    with open(inputfile, 'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind, textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceHtml3(fname):
    textToFind = '"]'
    textToReplace = "</td></tr>"
    file = fname

    inputfile = file
    with open(inputfile, 'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind, textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceHtml4(fname):
    textToFind = "', " + '"'
    textToReplace = "</td><td>"
    file = fname

    inputfile = file
    with open(inputfile, 'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind, textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)

def replaceHtml5(fname):
    textToFind = '"' + "', "
    textToReplace = "</td><td>"
    file = fname

    inputfile = file
    with open(inputfile, 'r') as inputfile:
        fileData = inputfile.read()
        freq = 0
        freq = fileData.count(textToFind)
    destibnationpath = file
    fileData = fileData.replace(textToFind, textToReplace)
    with open(destibnationpath, 'w') as file:
        file.write(fileData)