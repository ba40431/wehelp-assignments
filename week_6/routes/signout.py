from flask import Blueprint,Flask,request,redirect,render_template,session

signout_info=Blueprint("signout",__name__,static_folder="static",template_folder="templates")

@signout_info.route("/signout")
def signout():
    session["username"]=None
    return redirect("/")