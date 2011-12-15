#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
assign_project_name.py

see also http://www.dabeaz.com/generators/Generators.pdf

"""

from __future__ import with_statement
import os, re, gzip, bz2, fnmatch, fileinput

def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)

def gen_open(filenames):
    for name in filenames:
        if name.endswith(".gz"):
            yield gzip.open(name)
        elif name.endswith(".bz2"):
            yield bz2.BZ2File(name)
        else:
            yield open(name)

def gen_cat(sources):
    for s in sources:
        for item in s:
            yield item

def gen_grep(pat, lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line):
            yield line

def gen_subn(regex, replacewith, top):
    for path, dirlist, filelist in os.walk(top):
        print "+ Grepping %s ..." % path
        with fileinput.input(filelist, inplace=1) as fin:
            for fline in fin:
                print regex.subn(fline, replacewith)

def run(appname='core'):
    
    # First: rename files containing '__site__' by substituting
    # the appname (in lowercase) for the '__site__' marker.
    renamer = re.compile('(__site__)', re.MULTILINE)
    rename_targets = gen_find('__site__*', os.getcwd())
    
    for targ in rename_targets:
        print "+ Renaming %s ..." % targ
        os.move(targ, renamer.subn(str(appname.lower()), targ))
    
    # Next: substitute '__site__' markers within the code itself.
    #replace_targets = gen_find('*.*', os.getcwd())
    gen_subn(renamer, str(appname), os.getcwd())
    
    