#Jason Lin
#SoftDev1 pd07
#K08 -- Fill Yer Flask
#2018-09-19

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_page():
    return """<h1>Welcome to this website!</h1>
    <h3>I hope you enjoy your stay here.</h3>
    <p>If you want to look at a llama, <a href="/llama">click here.</a></p>
    <h2> But what if you do not like llamas?</h2>
    <p>Do not worry because we have <a href="/axolotl">axolotls too!</a></p>"""

@app.route("/llama")
def llama_page():
    return """<h1>My llama says Hi to you</h1>
    <img width="300" height="450" src="https://images.halloweencostumes.com/products/41458/1-1/adult-llama-costume1.jpg" alt="Oh no, the llama is invisible!"/>
    <h4>Your options:</h4>
    <a href="/">Go back home</a><br/>
    <a href="/axolotl">Check out the Axolotl.</a>
    """

@app.route("/axolotl")
def axolotl_page():
    return """<h1>This axolotl is very tired.</h1>
    <img width="480" height="380" src="https://i.imgur.com/wdzAJ9J.gif" alt="Oh no, the axolotl is yawning somewhere else!"/>
    <h4>Your options:</h4>
    <a href="/">Go back home</a><br/>
    <a href="/llama">Check out the llama.</a>
    """

if __name__ == "__main__":
    app.debug = True
    app.run()
