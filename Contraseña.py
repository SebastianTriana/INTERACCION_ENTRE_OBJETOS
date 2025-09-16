#Autor: Sebastián Triana

#Estos son ejercicios con clases POO

#Creacion de la clase contraseña

#importamos las librerias necesarias
import random
import string

class contraseña():
    #constructor
    def __init__(self):
        self.longitud = 8
        self.clave = ""
    
    #Metodo para generar la contraseña
    def generar(self):
        #De la libreria string usamos ascii_letters que contiene las letras del abecedario(MAyusculas y minusculas)
        #Tambien de string usamos digits que importa los numero del 0 al 9
        caracteres = string.ascii_letters + string.digits

        #Aqui elegimos y unimos los caracteres en base a la longitud(8)
        contraseña_aleatoria = "".join(random.choice(caracteres) for i in range(self.longitud))
        self.clave = contraseña_aleatoria
        self.valor = self.clave
    
    #Ahora miramos si es segura o no
    def segura(self):
        mayuscula = any(c.isupper() for c in self.valor)
        minuscula = any(c.islower() for c in self.valor)
        numero = any(c.isdigit() for c in self.valor)
        if mayuscula and minuscula and numero:
            return True
        else:
            return False

#Definimos el MAIN
def main():
    contraseña1 = contraseña()
    contraseña1.generar()
    print("Contraseña generada:", contraseña1.clave)
    if contraseña1.segura():
        print("La contraseña es segura")
    else:
        print("La contraseña no es segura")
if __name__ == "__main__":
    main()