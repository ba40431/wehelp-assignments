from flask import Blueprint,Flask,request,redirect,render_template,session
import mysql.connector

member_info=Blueprint("member",__name__,static_folder="static",template_folder="templates")

@member_info.route("/member/")
def member():
    username=session["username"]
    connection=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="12345678",
        database="website"
    )
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `member` WHERE `username`=%s ;",[username])
    member=cursor.fetchone()

    if member:
        if username==member[2]:
            return render_template("member.html",name=member[1])
    else:return redirect("/")

    cursor.close()
    connection.close()
