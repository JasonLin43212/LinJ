#Jason Lin
#SoftDev1 pd07
#K26 -- Getting More REST
#2018-11-14

from flask import Flask, render_template
import urllib, json, random
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    #New york times
    API_KEY_NYT = "57de9cbef9114384a1a0c114cfcff60b"
    URL_STUB_NYT = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=trump&api-key="
    URLNYT = URL_STUB_NYT + API_KEY_NYT
    #print(URLNYT)

    url_thing_nyt = urllib.request.urlopen(URLNYT)
    #print(url_thing_nyt);
    response = url_thing_nyt.read()
    #print(response)
    dict_nyt = json.loads(response)
    #print("=========================")
    #print("Dictionary")
    #print(dict)
    #print("=========================")
    #print(dict_nyt)
    #print("=========================")

    #memegenerator.net
    API_KEY_MEME = "5ccd24b9-9cd9-4703-b0ea-e6d4c1bc7380"
    URL_STUB_MEME = "http://version1.api.memegenerator.net//Instances_Search?q=drake&pageIndex=0&pageSize=4&apiKey="
    URLMEME = URL_STUB_MEME + API_KEY_MEME
    #print(URLMEME)

    url_thing_meme = urllib.request.urlopen(URLMEME)
    #print(url_thing_meme);
    response_meme = url_thing_meme.read()
    #print(response)
    dict_meme = json.loads(response_meme)

    #chuck norris joke
    URL_CHUCK = "http://api.icndb.com/jokes/random/3"

    url_thing_chuck = urllib.request.urlopen(URL_CHUCK)
    #print(url_thing_meme);
    response_chuck = url_thing_chuck.read()
    #print(response)
    dict_chuck = json.loads(response_chuck)


    return render_template("rest_page.html", NYT_array=dict_nyt["response"]["docs"],
                                             meme_array = dict_meme["result"],
                                             chuck_array = dict_chuck["value"])

if __name__ == "__main__":
    app.debug = True
    app.run()
