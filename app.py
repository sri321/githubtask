import requests
import json
from flask import Flask

#### Get the Name from API ####
data = requests.get('http://uinames.com/api/').json()

#### get Joke from API ####
jokedat = requests.get('http://api.icndb.com/jokes/random?firstName=John&lastName=Doe&limitTo=[nerdy]').json()

#### Convert data into required format ####
output = (data['name']+' '+data['surname']+' '+jokedat['value']['joke']).encode('ascii', 'ignore')

#### Testing API output####
#print (output)

#### Start WebService ####
app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>{name}!</h3>"
    return html.format(name=output)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
