# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import argparse
import obtainXml
import htmlCreation

if __name__ == '__main__':

    # Here we are creating the ARGS from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", help="Create the DB and xml", action="store_true")
    parser.add_argument("--render", help="Create the HtmlFile")
    args = parser.parse_args()

    # Here we process the arguments
    if args.rebuild == True:
        obtainXml.obtainXml()
    elif args.render != None:
        if args.render == '0':
            fname = args.render
            print('The archive ' + 'root' + '.html has been created.')
            htmlCreation.htmlCreation(fname)
        else:
            fname = args.render
            print('The archive ' + args.render + '.html has been created.')
            htmlCreation.htmlCreation(fname)
    else:
        print("No Arguments -h for help")
