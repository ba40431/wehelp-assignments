from flask import Flask,request,redirect,render_template,session
from error import error_message
from signout import signout_info
from member import member_info
from signin import signin_info

app=Flask(__name__)
app.secret_key="any string but secret"
app.register_blueprint(error_message)
app.register_blueprint(signout_info)
app.register_blueprint(member_info)
app.register_blueprint(signin_info)

@app.route("/")
def index():
    return render_template("index.html")


app.run(port=3000)