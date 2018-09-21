#Jason Lin
#SoftDev1 pd07
#K08 -- Fill Yer Flask
#2018-09-19

from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello_world():
    return "Hello, World"

if __name__ == "__main__":
    app.debug = True
    app.run()
