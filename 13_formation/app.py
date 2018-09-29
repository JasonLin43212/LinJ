#Jason Lin
#SoftDev1 pd07
#K13 -- Echo Echo Echo
#2018-09-28

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("formThing.html")


@app.route("/auth",methods=["GET","POST"])
def authenticate():
    request_dict = {}
    if request.method=="GET":
        request_dict = request.args
    else:
        request_dict = request.form
    return render_template("answer.html",
                           username=request_dict["username"],
                           method=request.method)

if __name__ == "__main__":
    app.debug = True
    app.run()
