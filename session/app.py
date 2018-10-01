#Jason Lin
#SoftDev1 pd07
#KNN -- TITLE
#201y-mm-dd

from flask import Flask, render_template, request ,session,url_for,redirect
import os
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    print(url_for('home'))
    return redirect(url_for("login"))#render_template("template.html")

@app.route("/auth", methods=["POST"]) 
def auth():
    username=request.form["username"]
    password= request.form["password"]
    if username == "Bob":
            if password=="pizza":
                return render_template("login.html",user=username)
            else:
                return render_template("error.html",error_message="Wrong password")
    else:
        return render_template("error.html",error_message="Wrong Username")

@app.route("/login")
def login():
    return render_template("login.html",user="bob")

if __name__ == "__main__":
    app.debug = True
    app.run()
