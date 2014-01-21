#!/usr/bin/env python
# encoding: utf-8
"""
concierge/__init__.py

Created by FI$H 2000 on 2011-12-20.
Copyright (c) 2011 Objects In Space And Time, LLC. All rights reserved.

"""

import types, collections

class option(object):
    def __init__(self, abbrev, default=False):
        self.abbrev = abbrev
        self.default = default
    
    def __call__(self, f, doc=None):
        self.f = f
        
        self.__doc__ = doc or f.__doc__
        self.__option__ = f.__name__
        self.__module__ = f.__module__
        
        return self
    
    def __repr__(self):
        return "+ %s ..." % self.__doc__.strip()
    
    def __get__(self, instance, owner):
        return getattr(instance, 'option_%s' % self.__option__)()


class Obsequious(type):
    
    def __new__(cls, name, bases, attrs):
        
        options = collections.OrderedDict()
        
        for attr_name, attr in attrs.items():
            if hasattr(attr, '__option__'):
                if attr.default is True:
                    if not '__default__' in attrs:
                        attrs['__default__'] = attr.__option__
                attrs['option_%s' % attr_name] = attr.f
                options[attr.abbrev] = repr(attr)
        
        attrs['options'] = options
        return super(Obsequious, cls).__new__(cls, name, bases, attrs)

class Amenity(object):
    
    __metaclass__ = Obsequious
    
    """ Configure this amenity? """
    
    @option('y')
    def yes(self):
        """ Setting up the amenity """
        raise NotImplemented("This Amenity needs a (yes) option.")
    
    @option('n')
    def no(self):
        """ Skipping the amenity """
        raise NotImplemented("This Amenity needs a (no) option.")
    
    @option('e', default=True)
    def ez(self):
        """ Setting up the amenity with the defaults """
        raise NotImplemented("This Amenity needs an (ez) option.")
    
    @property
    def default(self):
        return self.__class__.__dict__.get('option_%s' % self.__class__.__default__)(self)
    
    def __repr__(self):
        return self.__doc__.strip()





if __name__ == '__main__':
    class MyDick(Amenity):
        """ Suck on my diznick? """
        
        @option('y')
        def yes(self):
            """ Sucking my diznick """
            out = "Blowjob, bro!"
            return out
        
        @option('n', default=True)
        def no(self):
            """ Refraining from sucking on my diznick """
            out = "SPIDERMAN!!!"
            return out
        
        @option('e')
        def ez(self):
            """ Taking her to see Wicked """
            out = "LET'S BRO OUT!!"
            return out
    
    
    getsome = MyDick()
    
    print ""
    print repr(getsome)
    
    print ""
    print MyDick.options
    
    print ""
    print getsome.yes
    print getsome.no
    print getsome.ez
    
    print ""
    print MyDick.__dict__
    
    print ""
    print getsome.default
    
    
    
    

