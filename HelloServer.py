#!/usr/bin/env python
# modified from https://raw.githubusercontent.com/troeger/corba-example/master/python/server.py
import sys
from omniORB import CORBA, PortableServer
import HelloApp, HelloApp__POA

class HelloServer (HelloApp__POA.Hello):
  def sayHello(self):
   return "Hello world";

  def shutdown (self):
   sys.exit(0)

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")


ei = HelloServer()
eo = ei._this()

f = open("iorfile",'w')
f.write(orb.object_to_string(eo))
f.close()

poaManager = poa._get_the_POAManager()
poaManager.activate()

orb.run()

