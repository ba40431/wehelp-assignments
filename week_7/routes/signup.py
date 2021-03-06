from flask import Blueprint,Flask,request,redirect,render_template,session,flash
import mysql.connector
from connection import pool

signup_info=Blueprint("signup",__name__,static_folder="static",template_folder="templates")

@signup_info.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    register_username=request.form["register_username"]
    register_password=request.form["register_password"]

    connection=pool.connection()
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `member` WHERE `username`=%s ;",(register_username,))
    member=cursor.fetchone()

    if member==None:
        if register_username==''or register_password=='' or name=='':
            return redirect("/error/?message=請輸入姓名、帳號和密碼")
        else:
            cursor.execute("INSERT INTO `member`(`name`,`username`,`password`) VALUES (%s,%s,%s);",
            (name, register_username,register_password)) #%s 利用佔位符傳遞參數，防範SQL injection
            cursor.close()
            connection.commit()
            connection.close()
            flash("恭喜註冊成功","info")
            return redirect("/")
    if member:
        if register_username==member[2]:
            return redirect("/error/?message=帳號已經被註冊")

    cursor.close()
    connection.close()
