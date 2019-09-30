import requests
import json
from flask import Flask

def getdata():
    try:
        #### Get the Name from API ####
        data = requests.get('http://uinames.com/api/').json()
        #### get Joke from API ####
        jokedat = requests.get('http://api.icndb.com/jokes/random?firstName=John&lastName=Doe&limitTo=[nerdy]').json()
        #### Convert data into required format ####
        output = (jokedat['value']['joke'].replace('John Doe',data['name']+' '+data['surname'])).encode('ascii', 'ignore')
    except:
        data = requests.get('http://uinames.com/api/')
        if data.status_code == 429:
            output = "Too Many Requests please wait and Try again"
    return output

#### Testing API output ####
#print (output)

#### Start WebService ####
app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>{name}!</h3>"
    return html.format(name=getdata())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
