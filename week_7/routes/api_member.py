from flask import Blueprint,Flask,request,redirect,render_template,session,flash,jsonify
import mysql.connector
import json
from connection import pool

api_member=Blueprint("api_member",__name__,static_folder="static",template_folder="templates")

@api_member.route("/api/member",methods=["POST"])
def update_member():
    member_data=json.loads(request.get_data())
    name = member_data["name"]

    if session["username"]:
        session["name"]=name
        connection=pool.connection()
        cursor=connection.cursor()
        cursor.execute("UPDATE `member` SET `name`=%s WHERE `username`=%s;",(name,session["username"]))
        member=cursor.fetchone()
        cursor.close()
        connection.commit()
        connection.close()
        data={"ok":True}
        return jsonify(data)
    if session["username"]==None:
        data={"error":True}
        return jsonify(data)


    cursor.close()
    connection.close()
