#Autor: Sebastián Triana

#Estos son ejercicios con clases POO

#Creacion de la clase persona

class persona():
    #Constructor
    def __init__(self, nombre, edad, genero, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.peso = peso
        self.altura = altura
    
    #Metodo para calcular el IMC
    def calcular_IMC(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    #Metodo para determinar mayoria de edad
    def mayoria_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
#Definimos el MAIN
def main():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    genero = input("Ingrese su genero (M/F): ")
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))

    persona1 = persona(nombre, edad, genero, peso, altura)

    imc = persona1.calcular_IMC()
    print(f"{persona1.nombre}, su IMC es: {imc:.2f}")

    if persona1.mayoria_edad():
        print(f"{persona1.nombre} es mayor de edad.")
    else:
        print(f"{persona1.nombre} es menor de edad.")

if __name__ == "__main__":
    main()