#!/usr/bin/env python

""" File: file_handling.py
	Author: Sarah Lindner
	Date of last change: 26.05.2015

	Useful functions for file handling (modifying file name etc.).
"""

import os

def path_filename( file ):
	path_filename = os.path.dirname( os.path.realpath( file ) ) + "/" + os.path.basename( file )
	return path_filename

def filestub( file ):
	splitfile = os.path.basename( file ).split('.')
	filestub = splitfile[len(splitfile)-2] # take item before last dot
	return filestub

def extension( file ):
	splitfile = os.path.basename( file ).split('.')
	extension = splitfile[len(splitfile)-1] # take item after last dot
	return extension
	

def pathname( file ):
	pathname = os.path.dirname( os.path.realpath( file ) )
	return pathname


def check_overwrite( file ):
    if os.path.isfile(filename_handling.path_filename(file)):
        response = raw_input("Overwrite " + file + " ? - y/n\n")
        if response.lower().startswith("n"):
            print("Sayoonara")
            exit()
