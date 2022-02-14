from flask import Blueprint,Flask,request,redirect,render_template,session,flash,jsonify
import mysql.connector
from connection import pool

api_members=Blueprint("api",__name__,static_folder="static",template_folder="templates")

@api_members.route("/api/members")
def api():
    username=request.args.get("username")

    connection=pool.connection()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `member` WHERE `username`=%s ;",[username])
    member=cursor.fetchone()

    if member:
        data={"data":{
                "id":member[0],
                "name":member[1],
                "username":member[2]
            }}
        return jsonify(data)
    if member==None:
        data={"data":None}
        return jsonify(data)
    
    cursor.close()
    connection.close()

    
