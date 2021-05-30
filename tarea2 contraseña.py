contr = input("\nIngresa una contraseña:\n")
p=input("\nPara poder continuar vuelve ingresa tu contraseña: \n")
if (contr.lower () == p.lower ()):
    print("Contraseña Correcta.")
else:
    print("Contraseña incorrecta.\nVolver a intentar.")
        
