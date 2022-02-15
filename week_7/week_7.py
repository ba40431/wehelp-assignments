from flask import Flask,request,redirect,render_template,session
from routes.error import error_message
from routes.signout import signout_info
from routes.member import member_info
from routes.signin import signin_info
from routes.signup import signup_info
from routes.api_members import api_members
from routes.api_member import api_member

app=Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key="any string but secret"
app.register_blueprint(error_message)
app.register_blueprint(signout_info)
app.register_blueprint(member_info)
app.register_blueprint(signin_info)
app.register_blueprint(signup_info)
app.register_blueprint(api_members)
app.register_blueprint(api_member)

@app.route("/")
def index():
    return render_template("index.html")


app.run(port=3000)