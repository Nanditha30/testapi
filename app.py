from flask import Flask
from flask_restful import Api
from resourses.emp import Emp
import pymysql

app=Flask(__name__)

'''@app.route('/')
def home():
    connection=pymysql.connect(host='localhost',
                                user='root',
                                password='Nanditha@1',
                                db='testapi',
                                cursorclass=pymysql.cursors.DictCursor)
    mycursor=connection.cursor()
    mycursor.execute('select*from testapi.emp;')
    return str(mycursor.fetchall())'''
api=Api(app)
api.add_resource(Emp,'/emp')
app.run(port='8080',debug='true')
