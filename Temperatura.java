/******************************************************************************
temp=float(input("Temperatura registrada"))
if temp>=27: print("Pongase algo fresco ")
elif temp>=20 and temp<27: print("Abrigate🧥")
elif temp>=16 and temp<20: print("Abrigate mas🧥🧣")
else: print("Esta helando🥶🥶🥶")
                   
*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    
		System.out.println("Temperatura registrada: ");
		Scanner leer =new Scanner(System.in);
		//nextLint es para String
		//nextFloat es para leer decimales
		float temp = leer.nextFloat();
		//&& and || or 
		if(temp>=27){System.out.println("Pongase algo fresco ");}
		else if (temp>=20 && temp<27){System.out.println("Abrigate🧥");}
		else if (temp>=16 && temp<20){System.out.println("Abrigate mas🧥🧣");}
		else {System.out.println("Esta helando🥶🥶🥶");}
		
		//Ejercicio para easy hand if
	    System.out.println("Cual es tu edad?");
	    int edad = leer.nextInt();
	    System.out.println(edad>=18? "Eres mayor de edad👵":"Eres menor de edad👶");
		
	}
}