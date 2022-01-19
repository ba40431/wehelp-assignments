from flask import Blueprint,Flask,request,redirect,render_template,session

signin_info=Blueprint("signin",__name__,static_folder="static",template_folder="templates")

@signin_info.route("/signin",methods=["POST"])
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