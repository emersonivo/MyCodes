#!/usr/lib/python2.7
import ConfigParser

global config
config = ConfigParser.ConfigParser()
config.read('defaults.cfg')

class bola:
    def pbola(self, x, y):
        print "From first.bola: ", v

class sola:
    def fsola(self, x):
        print "From first.sola: ", x

x = config.sections()[0]
dir(x)