Ejemplo de https://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html

Pasos:

1. idlj -fall  Hello.idl
2. javac *.java HelloApp/*.java
3. orbd -ORBInitialPort 1050&
4. java HelloServer -ORBInitialPort 1050 -ORBInitialHost localhost&
5. java HelloClient -ORBInitialPort 1050 -ORBInitialHost localhost

