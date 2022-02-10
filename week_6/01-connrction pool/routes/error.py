from flask import Blueprint,Flask,request,redirect,render_template,session

error_message=Blueprint("error",__name__,static_folder="static",template_folder="templates")

@error_message.route("/error/")
def error():
    error_message=request.args.get("message","自訂的錯誤訊息")  
    return render_template("error.html",message=error_message)