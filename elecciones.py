#Programa que elegirá tus comidas diarias
import random

def run():    
#Menu del programa
    menu = """Bienvenido a nuestro selector aleatorio de comida, 
    que quieres que elijamos?
    1. Desayuno.
    2. Almuerzo.
    3. Cena.
    4. Postre.
    5. Hazme el menu del día!!! (En Beta)
    """
    numero = input(menu)
#Opciones dependiendo de la respuesta del usuario    
# Desayuno    
    if numero == "1":
        comidas = ["Huevos", "Cereal", "Calentado", "fruta"]
        Seleccion= random.choice(comidas)
        print("Hoy desayunarás: " + Seleccion + ".")
        exit (0)

#Almuerzo
    elif numero == "2":
        comidas = ["Ajiaco", "Bandeja Paisa", "Arroz con pollo", "Sudado de pollo"]
        Seleccion= random.choice(comidas)
        print("Hoy almorzarás: " + Seleccion + ".")
        exit (0)

#Cenas
    elif numero == "3":
        comidas = ["Sandwiches", "Cremas", "Sopa de pollo"]
        Seleccion= random.choice(comidas)
        print("Hoy cenarás: " + Seleccion + ".")
        exit (0)

#Postres
    elif numero == "4":
        comidas = ["helado", "postre 3 leches", "Flan", "postre de Arequipe"]
        Seleccion= random.choice(comidas)
        print("Hoy tu postre será: " + Seleccion + ".")    
        exit (0)

#Comida completa del día
    elif numero == "5":
        comida = ["Huevos", "Cereal", "Calentado", "fruta"]
        comida2 = ["Ajiaco", "Bandeja Paisa", "Arroz con pollo", "Sudado de pollo"]
        comida3 = ["Sandwiches", "Cremas", "Sopa de pollo"]
        comida4 = ["helado", "postre 3 leches", "Flan", "postre de Arequipe"]
        desayuno= random.choice(comida)
        almuerzo= random.choice(comida2)
        comida= random.choice(comida3)
        postre= random.choice(comida4)
        print("""Tu menu completo será: 
        Desayuno= """ + desayuno + """.
        Almuerzo= """ + almuerzo + """.
        Cena= """ + comida + """.
        Postre= """ + postre + """.
        Hemos terminado!!!""") 
        exit (0)

#Error
    else:
        print("""Ingresa un valor válido, por favor.

Intentemoslo de nuevo, te parece?
""")
    run()  


if __name__ == '__main__':
    run()
