Ejemplo de https://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html y manual de OmniORB

Pasos para acceder de java a java y de python a java
-----
```
1. idlj -fall  Hello.idl
2. javac *.java HelloApp/*.java # compila todas las clases
3. orbd -ORBInitialPort 1050 & # lanza el  ORB
4. java HelloServer -ORBInitialPort 1050 -ORBInitialHost 127.0.0.1& # lanza el servidor
5. catior `cat iorfile` # comprueba que el fichero iorfile tiene la referencia al servidor
6. java HelloClient -ORBInitialPort 1050 -ORBInitialHost 127.0.0.1 #imprimirá la cadena devuelta por el servidor 
7. java HelloClient quit -ORBInitialPort 1050 -ORBInitialHost 127.0.0.1 #apagar el servidor
```

Para el cliente python (el servidor ya está compilado):
```
1. omniidl -bpython Hello.idl # genera el stub para python. Sólo usaremos el cliente
2. java HelloServer -ORBInitialPort 1050 -ORBInitialHost 127.0.0.1& # lanza el servidor
3. python HelloClient.py # imprimirá la cadena devuelta por el servidor
4. python HelloClient.py quit # apagar el servidor
```
Pasos para acceder de python a python y de java a python, una vez ejecutados los pasos anteriores
-----
```
1. omniidl -bpython Hello.idl # genera el stub para python. Usaremos cliente y servidor
2. orbd -ORBInitialPort 1050 & # lanza el  ORB, pero sólo si no se ha lanzado antes
3. python HelloServer.py
4. catior `cat iorfile` # comprueba que el fichero iorfile tiene la referencia al servidor
5. java HelloClient -ORBInitialPort 1050 -ORBInitialHost 127.0.0.1 #imprimirá la cadena devuelta por el servidor 
6. python HelloClient.py # imprimirá la cadena devuelta por el servidor
7. python HelloClient.py quit# apaga el servidor
```

Requisitos
----------
Tener instalado JDK 1.8

	sudo apt install openjdk-8-jdk

Instalado python 2.7. Omniorb sólo funciona con 2.7

	sudo apt install libomniorb4-1 omniorb python-omniorb python-omniorb-dbg python-omniorb-doc python-omniorb-omg






