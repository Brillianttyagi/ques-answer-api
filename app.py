from flask import Flask,jsonify
from bs4 import BeautifulSoup
import requests as rq
app = Flask(__name__)

@app.route('/<string:string>')
def get_answer(string):
    page = rq.get("https://www.google.com/search?q="+string)

    soup = BeautifulSoup(page.content,'html.parser')
    result = soup.find('div',class_='BNeawe s3v9rd AP7Wnd')

    result = list(result.text.split('.'))
    return jsonify(answer=result[0])
@app.route('/')
def home():
    return "<h4>enter your question after slash of domain name.thankyou<h4>"

if __name__ == "__main__":
    app.run(debug=True)