#!/usr/bin/python3
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    '''Determines if an object is an inherited instace of a class.'''
    return isinstance(obj, a_class) and type(obj) != a_class
