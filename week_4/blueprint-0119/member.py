from flask import Blueprint,Flask,request,redirect,render_template,session

member_info=Blueprint("member",__name__,static_folder="static",template_folder="templates")

@member_info.route("/member/")
def member():
    if session["username"]=="test":
        return render_template("member.html")
    else:return redirect("/")