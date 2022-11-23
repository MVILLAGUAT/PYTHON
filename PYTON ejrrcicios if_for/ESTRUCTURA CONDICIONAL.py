print("BINBENIDO!!!!!!!!");
print("1) ingresar dos valores e indecar cual de los 2 valores es el mayo y cual es el menor.");
print("2) ingresat tres valores e indicar cual de los 3 valores es el mayor.");
print("3) solicitar 3 valores numericos e indicar si la suma de los calores es multiplo de 7.");
print("4) ingreso de tres numeros monresr el prodedio si esto es par o impar.");
print("5) calcular cobro de un clinete.");

opcion=int(input("INGRESE SU OPCION :"));
if(opcion==1):
    num1 = int(input("INGRESE UN NUMERO ENTERO :"));
    num2 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    if(num1>num2):
        print("EL NUMERO MAYOR ES:", num1);
        print("EL NUMERO MENOR ES:", num2)
    elif(num1<num2):
        print("EL NUMERO MENOR ES:", num1);
        print("EL NUMERO MAYOR ES:", num2);
    else:
        print("LOS NUMEROS SON IGUALES", num1, "=", num2);
elif(opcion==2):
    num0 = int(input("INGRESE UN NUMERO ENTERO :"));
    num3 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    num4= int(input("INGRESE OTRO NUMERO ENTERO :"));
    if(num0>num3):
        if(num0>num4):
            print("EL NUMERO MAYOR ES:", num0);
    elif(num3>num0):
        if(num3>num4):
            print("EL NUMERO MAYOR ES :", num3);
    else:
            print("EL NUMERO MAYOR ES .", num4);
elif(opcion==3):
    num5 = int(input("INGRESE UN NUMERO ENTERO :"));
    num6 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    num7 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    suma=(num5+num6+num7);
    if(suma % 7 == 0):
            print("LA SUMA DE LOS NUMEROS ES MULTIPLO DE 7 :", suma);
    else:
            print("LA SUMA DE LOS  NUMEROS NO ES MULTIPLO DE 7 :", suma);
elif(opcion==4):
    num8 = int(input("INGRESE UN NUMERO ENTERO :"));
    num9 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    num10 = int(input("INGRESE OTRO NUMERO ENTERO :"));
    suma=(num8+num9+num10);
    promedio=(suma/3);
    if(promedio % 2 == 0):
            print("EL PROMEDIO DE LOS NUMEROS ES PAR: ", promedio);
    else:
            print("EL PROMEDIO DE LOS NUMEROS ES IMPAR :", promedio);
elif(opcion==5):
                   nomre=input("INGRESE SU NOMBRE :");
                   nacional=int(input("Ingres los minutos nacionales consumidos :"));
                   internacional=int(input("Ingrse los minutos internacionales consumido :"));
                   suma=nacional+internacional;
                   total=0;

                   if (suma<=25):
                            print("minutos gratis don :",nomre);
                   elif(nacional<=25):
                            acu=nacional-25
                            internacional+=acu;
                            total=internacional*2.5;
                   else:
                                        nacional-=25;
                                        total=(nacional*0.5)+(internacional*2.5);
                                        print(nomre,"TOTAL A PAGAR Q",total);
else:
                print("SU OPCION ES INCORECTO !!!!!:");

