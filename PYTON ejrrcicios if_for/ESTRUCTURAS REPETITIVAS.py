print("¡¡¡¡¡BIENBENIDO A LA ESTRUCTURAS REPETITIVAS!!!!! :");
print("1)MOSTRAT UNA TABLA DE MULTIPLICACION POR EL USUARIO :");
print("2)mostrar el listado de numeros impares de 1 hasta un valosr maximo inresado por el usuario.");
print("3)montesr los numeros multiplos de un numero ingresado por el usuario rango 1 a 1000.");
opcion=int(input("INGRESE SU OPCION :"));
if(opcion==1):
    tabla=int(input("INGRESE LA TABLA DE MULTIPLICAR QUE DESEE :"));
    inicio=int(input("INGRESE EL INICIO DE LA TABLA :"));
    final=int(input("INGRESE EL FINAL DE LA TABLA :"));

    for i in range(inicio,final+1):
        resultado=(tabla*i);
        print(tabla,"*",i ,"=", resultado);
elif(opcion==2):
    final=int(input("Ingrese el ultimo numero"));

    for i in range(1,final+1):
        if(i%2==1):
            print(i);
elif(opcion==3):
    multilos=int(input("INGRESE EL MULTIPLO :"));

    for i in range(1,100+1):
        if(i%multilos==0):
            print(i);
else:
    print("SU OPCION  ES INCORECTA !!!!!!:");