#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
assign_project_name.py

see also http://www.dabeaz.com/generators/Generators.pdf

"""

TEXT_TARGETS = ('py', 'js', 'txt', 'xml', 'html', 'css', 'md', 'rst',)


from __future__ import with_statement
import sys, os, re, gzip, bz2, fnmatch, fileinput

def gen_find(filepat, top):
    for pth, dirlist, filelist in os.walk(top):
        for dr in dirlist:
            if dr.startswith('.'):
                dirlist.remove(dr)
        for name in fnmatch.filter(filelist+dirlist, filepat):
            yield os.path.join(pth, name)

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
    for pth, dirlist, filelist in os.walk(top):
        for dr in dirlist:
            if dr.startswith('.'):
                dirlist.remove(dr)
        
        print "+ Grepping %s ..." % pth
        
        os.chdir(pth)
        for fline in fileinput.input([f for f in filelist if f.split('.')[-1:].lower() not in TEXT_TARGETS], inplace=1):
            print regex.subn(fline, replacewith)

def main(appname='core'):
    
    # First: rename files containing '__site__' by substituting
    # the appname (in lowercase) for the '__site__' marker.
    renamer = re.compile('(__site__)', re.MULTILINE)
    rename_targets = gen_find('__site__*', os.getcwd())
    
    for targ in rename_targets:
        print "+ Renaming %s ..." % targ
        os.rename(targ, renamer.subn(str(appname.lower()), targ)[0])
    
    # Next: substitute '__site__' markers within the code itself.
    #replace_targets = gen_find('*.*', os.getcwd())
    gen_subn(renamer, str(appname), os.getcwd())

if __name__ == "__main__":
    main(*sys.argv[1:])


