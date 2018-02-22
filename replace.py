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
    textToFind = "('"
    textToReplace = "<tr><td>"
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
    textToFind = "', '"
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
    textToFind = "')"
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