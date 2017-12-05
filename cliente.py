#! /usr/bin/env python

import HelloApp
import CORBA
import sys



## this should no longer be needed, but is here as workaround to
## http://bugzilla.gnome.org/show_bug.cgi?id=323201
## you also need to use this if the server is not ORBit2 based

#import Test  # use this if the server is not ORBit2 based

orb = CORBA.ORB_init()

ior = file('iorfile').read()
print(ior)
echo = orb.string_to_object(ior)


print repr(echo)

#echo=echo._narrow(Hello) # _narrow not needed with ORBit2 servers

if len(sys.argv) >1 and sys.argv[1] == 'quit':
    echo.shutdown()
else:
    echo.sayHello()

