// Copyright and License 
// Modificado de https://docs.oracle.com/javase/7/docs/technotes/guides/idl/jidlExample.html
 
import HelloApp.*;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import static java.lang.System.out;
import static java.nio.file.Files.readAllBytes;
import static java.nio.file.Paths.get;

public class HelloClient
{
  static Hello helloImpl;

  public static void main(String args[]) throws Exception
    {
      try{
        // create and initialize the ORB
        ORB orb = ORB.init(args, null);


        helloImpl = HelloHelper.narrow(orb.string_to_object(new String(readAllBytes(get("iorfile")))));

        System.out.println("Obtained a handle on server object: " + helloImpl);
	if (args.length>1 && args[0].equalsIgnoreCase("quit"))
		helloImpl.shutdown();
	else
	        System.out.println(helloImpl.sayHello());
       


        } catch (Exception e) {
          System.out.println("ERROR : " + e) ;
          e.printStackTrace(System.out);
          }
    }

}
