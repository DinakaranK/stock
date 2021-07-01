import requests
from bs4 import BeautifulSoup
from flask import Flask,jsonify

app = Flask(__name__)

URL = "https://www.fresherscamp.com/category/off-campus-jobs/"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib

@app.route('/s.json')
def index():
    link1 = []
    for a in soup.find_all('h3', class_="entry-title td-module-title"):
        for i in a:
            link1.append(i['href'])

    dic = {}
    for i in range(len(link1)):
        dic[i] = link1[i]

    return jsonify(dic)


if __name__ == '__main__':
   app.run(debug = True)
