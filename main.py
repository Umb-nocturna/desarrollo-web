import os
#import mysql.connector #pip install mysql-connector-python
#from datetime import date
from functools import wraps
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SECRET_KEY'] = "mitoken"

""""
def per_guardar(id = 0, nombre = "John Doe", fuerza = 0, inteligencia = 0, defensa = 0, vida = 0):
    hoy = date.today()
    mydb = mysql.connector.connect(
        host="",
        user="",
        password="",
        database="",
        port=0
    )
    mycursor = mydb.cursor()
    print(mydb)
    sql = "INSERT INTO personaje2 (id, nombre,fuerza,inteligencia,defensa,vida,fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (id, nombre, fuerza, inteligencia, defensa, vida, str(hoy))
    mycursor.execute(sql,val)
    mydb.commit()
    return True
""""


def token_required(f):
     @wraps(f)
     def validate(*args, **kwargs):
         #set API_PKEY=mytoken
         token = request.headers['token']
         if token == app.config['SECRET_KEY']:
             return f(*args, **kwargs)
         else:
             return jsonify({"message":"token is invalid"}), 403    
     return validate 




@app.route('/')
@token_required
def index():
    return jsonify({"Choo Choo": "Welcome class"})

@app.route('/personaje')
@token_required
def personaje():
    return jsonify({"Choo Choo": "Personaje class"})
    #response = per_guardar(161200101,"Andrey", 17, 16, 15, 14)
    #if(response):
    #   return jsonify({"sucess": "Inserto personaje class"})
    #else:
    #    return jsonify({"error": "No insertado"})



"""
MAIN ...........................................................................
"""
if __name__ == '__main__':
    #app.run()
    app.run(debug=True, port=os.getenv("PORT", default=5000 )) 