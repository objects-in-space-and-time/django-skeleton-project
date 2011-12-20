
## timer
import time
t1 = time.time()

## setup django
from django.core.management import setup_environ
import settings.superlocal
setup_environ(settings.superlocal)

from django.conf import settings
from django.contrib.auth.models import User

## import ost2 specifics
from ost2.forsale.models import FSItem, FSImage, FSAmazonDataset, FSUserProfile
from ost2.forsale.models import FSOffer, FSISBNDBDataset, FSCoverset, FSInvitation
from ost2.forsale.models import FSQueuedEmail, FSItemLike
#from ost2.forsale.models import FSCronTask

from ost2.blog.models import SBBlog, SBEntry, SBImage, SBFootnote
from ost2.portfolio.models import AXCategory, AXItem, AXImage, AXFlashMorsel
from imagekit.models import ICCModel

## web scraping stuff
from BeautifulSoup import BeautifulSoup
import os, sys, re, urllib2, numpy, redis, xerox

## amazon ecs query interface thing
from ost2.utils.amazon import aws

from haystack.query import SearchQuerySet
hayq = lambda modl: SearchQuerySet().models(modl)

## friends forever
karel = FSItem.objects.get(title__icontains='drukwerk')
fish = User.objects.get(username='fish')

## monkeypatched color
#from ost2.utils.monkeypatch import monkeypatch
from imagekit import colors

import signalqueue
signalqueue.autodiscover()


## how long... has this been... going on?
t2 = time.time()
dt = str((t2-t1)*1.00)
dtout = dt[:(dt.find(".")+4)]
print ">>> Welcome to OST - Startup Time %ssec" % dtout


