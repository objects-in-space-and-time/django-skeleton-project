#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
assign_project_name.py

see also http://www.dabeaz.com/generators/Generators.pdf

"""
from __future__ import with_statement
import sys, os, re, gzip, bz2, fnmatch, fileinput

TEXT_TARGETS = ('py', 'js', 'txt', 'xml', 'html', 'css', 'md', 'rst',)


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
        
        
        os.chdir(pth)
        
        grepfiles = [f for f in filelist if f.split('.')[-1:][0].lower() in TEXT_TARGETS]
        if len(grepfiles) > 0:
            print "+ Grepping %s ..." % pth
            for fline in fileinput.input(grepfiles, inplace=1):
                if regex.search(fline):
                    print regex.subn(fline, replacewith)[0]
                else:
                    print fline

def main(appname='core'):
    
    # First: rename files containing '__site__' by substituting
    # the appname (in lowercase) for the '__site__' marker.
    renamer = re.compile('(__site__)')
    rename_targets = gen_find('__site__*', os.getcwd())
    
    for targ in rename_targets:
        print "+ Renaming %s ..." % targ
        os.rename(targ, renamer.subn(str(appname.lower()), targ)[0])
    
    print ""
    
    # Next: substitute '__site__' markers within the code itself.
    #replace_targets = gen_find('*.*', os.getcwd())
    gen_subn(renamer, str(appname), os.getcwd())

if __name__ == "__main__":
    main(*sys.argv[1:])


