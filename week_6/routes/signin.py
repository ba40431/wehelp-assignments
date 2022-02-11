from flask import Blueprint,Flask,request,redirect,render_template,session
import os
from dotenv import load_dotenv
import mysql.connector

signin_info=Blueprint("signin",__name__,static_folder="static",template_folder="templates")

@signin_info.route("/signin",methods=["POST"])
def signin():
    username=request.form["username"]
    password=request.form["password"]

    load_dotenv(".env")
    connection=mysql.connector.connect(
        host=os.getenv("host"),
        port=os.getenv("port"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )
    
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `member` WHERE `username`=%s ;",[username])
    member=cursor.fetchone()

    if member==None:
        if username==''or password=='':
            return redirect("/error/?message=請輸入帳號、密碼")
        else:return redirect("/error/?message=帳號或密碼輸入錯誤")
    if member: #有值
        if username==member[2] and  password==member[3]:
            session["username"]= username
            session["name"]=member[1]
            return redirect("/member/")
        elif username==''or password=='':
            return redirect("/error/?message=請輸入帳號、密碼")
        else:
            return redirect("/error/?message=帳號或密碼輸入錯誤")

    cursor.close()
    connection.close()