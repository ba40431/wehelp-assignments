from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from flask import session

app=Flask(__name__)

app.secret_key="any string but secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def signin():
    account_number=request.form["account_number"]
    password=request.form["password"]

    if account_number=="test" and  password=="test":
        session["username"]= account_number
        return redirect("/member/")
    
    elif account_number=='' or  password=='':
        return redirect("/error/?message=請輸入帳號、密碼")

    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")
        
@app.route("/signout")
def signout():
    session["username"]=None
    return redirect("/")

@app.route("/member/")
def member():
    if session["username"]=="test":
        return render_template("member.html")
    else:return redirect("/")

@app.route("/error/")
def error():#message=自訂的錯誤訊息
    error_message=request.args.get("message","自訂的錯誤訊息")  
    return render_template("error.html",message=error_message)

app.run(port=3000)