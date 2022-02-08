from flask import Blueprint,Flask,request,redirect,render_template,session,flash
import mysql.connector

signup_info=Blueprint("signup",__name__,static_folder="static",template_folder="templates")

@signup_info.route("/signup",methods=["POST"])
def signup():
    name=request.form["name"]
    register_username=request.form["register_username"]
    register_password=request.form["register_password"]
    connection=mysql.connector.connect(
        host="localhost",
        port="3306",
        user="root",
        password="12345678",
        database="website"
    )
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM `member`;")
    members=cursor.fetchall()
    for member in members:
        if register_username==member[2]:
            return redirect("/error/?message=帳號已經被註冊")

    if register_username=='' or  register_password=='' or name=='':
        return redirect("/error/?message=請輸入姓名、帳號和密碼")

    else:
        cursor.execute("INSERT INTO `member`(`name`,`username`,`password`) VALUES (%s,%s,%s);",
        (name, register_username, register_password)) #%s 利用佔位符傳遞參數
        cursor.close()
        connection.commit()
        connection.close()
        flash("恭喜註冊成功","info")
        return redirect("/")