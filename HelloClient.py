#! /usr/bin/env python

import HelloApp
import CORBA
import sys

orb = CORBA.ORB_init(sys.argv,CORBA.ORB_ID)

ior = file('iorfile').read()
echo = orb.string_to_object(ior)

if echo is None:
  print "Can't narrow reference."
  sys.exit(1)

if len(sys.argv) >1 and sys.argv[1] == 'quit':
    echo.shutdown()
else:
    print(echo.sayHello())
