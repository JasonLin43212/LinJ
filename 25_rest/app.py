#Jason Lin
#SoftDev1 pd07
#K25 -- Getting More REST
#2018-11-14

from flask import Flask, render_template
import urllib, json, random
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    API_KEY = "db4cae8bb9ae115d264c615af0cfe458"
    API_ID = "79b7edee"
    URL_STUB = "https://api.edamam.com/search?q=chicken&app_id="
    URL = URL_STUB + API_ID + "&app_key=" + API_KEY
    print(URL)

    url_thing = urllib.request.urlopen(URL)
    #print(url_thing);
    response = url_thing.read()
    #print(response)
    dict = json.loads(response)
    #print("=========================")
    #print("Dictionary")
    #print(dict)
    #print("=========================")
    #print("recipies")
    #print(dict["hits"][0]["recipe"])
    #print("=========================")

    return render_template("rest_page.html", recipe=dict["hits"][0]["recipe"])

if __name__ == "__main__":
    app.debug = True
    app.run()
