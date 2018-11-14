#Jason Lin
#SoftDev1 pd07
#K24 -- A RESTful Journey Skyward
#2018-11-13

from flask import Flask, render_template
import urllib, json, random
app = Flask(__name__) # instantiates an instance of Flask

@app.route("/") #Linking a function to a route
def home():
    year = str(random.randint(2010,2017))
    month = random.randint(1,12)
    if month < 10:
        month = "0" + str(month)
    else:
        month = str(month)
    day = random.randint(1,27)
    if day < 10:
        day = "0" + str(day)
    else:
        day = str(day)
    url_thing = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?date="+year+"-"+month+"-"+day+"&api_key=2iwjmYSb2rRld4YpBkhu3pFsi0UDd2qa2gkKKmYj")
    #print(url_thing);
    response = url_thing.read()
    #print(response)
    dict = json.loads(response)
    print(dict)
    img_url = dict["url"]
    name = dict["title"]
    date_taken = dict["date"]
    summary = dict["explanation"]
    return render_template("rest_page.html",url=img_url, title=name, date=date_taken, explanation=summary)

if __name__ == "__main__":
    app.debug = True
    app.run()
