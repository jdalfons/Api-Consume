# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Juan Diego Alfonso Ocampo
import argparse
import viewController
import controller
import model


if __name__ == '__main__':

    # Here we are creating the ARGS from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", help="Create the DB and xml", action="store_true")
    parser.add_argument("--render", help="Create the HtmlFile use --render [IDCategories]")
    args = parser.parse_args()

    # Here we process the arguments
    if args.rebuild == True:
        #obtainXml.obtainXml()
        controller.obtainXmlandcreatetable()
    elif args.render != None:
        fname = args.render
        print('The archive ' + args.render + '.html has been created in the folder html')
        viewController.htmlCreation(fname)
    else:
        print("No Arguments -h for help")
