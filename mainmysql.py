#https://www.youtube.com/watch?v=JVNirg9qs4M
import mysql.connector
from datetime import date
import os
from dotenv import load_dotenv

class Personaje:

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza:", self.fuerza)
        print("Inteligencia:", self.inteligencia)
        print("Defensa:", self.defensa)
        print("Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def guardar(self):
        #hoy = date.today()
        mydb = mysql.connector.connect(
            host="",
            user="",
            password="",
            database="",
            port=0
        )
        mycursor = mydb.cursor()
        print(mydb)
        sql = "INSERT INTO personaje (nombre,fuerza,inteligencia,defensa,vida,fecha) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.nombre, self.fuerza, self.inteligencia, self.defensa, self.vida, str(hoy))
        mycursor.execute(sql,val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")



if __name__ == '__main__':
    load_dotenv()
    mi_personaje = Personaje("Andrey",161200101,7,5,6)
    #mi_personaje.atributos()
    mi_personaje.subir_nivel(3,5,8)
    mi_personaje.guardar()
    #mi_personaje.atributos()