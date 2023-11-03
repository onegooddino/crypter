from flask import Flask, render_template,request
import utils
from utils import preprocessdata
import requests


urlcurr = "https://tokeninsight-crypto-api1.p.rapidapi.com/api/v1/simple/supported_vs_currencies"
urlcrypt = "https://tokeninsight-crypto-api1.p.rapidapi.com/api/v1/coins/list"

headers = {
	"TI_API_KEY": "a6853f07b5674e5ab026c71b60eb9851",
	"X-RapidAPI-Key": "8aad4b057fmsh56724249e744955p16f23bjsne38aa4af1764",
	"X-RapidAPI-Host": "tokeninsight-crypto-api1.p.rapidapi.com"
}

curr = requests.get(urlcurr, headers=headers).json()['data']
crypt = [item['name'] for item in requests.get(urlcrypt, headers=headers).json()['data']['items']]

print(curr)
print(crypt)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html",cu=curr,cr=crypt)

@app.route('/predict/', methods=['GET', 'POST'])

def predict():  
    if request.method == 'POST': 
        fromC = request.form.get('crypto')  
        toC = request.form.get('currency')  
        days = request.form.get('days')  


        prediction = utils.preprocessdata(fromC,toC,days)
        print(prediction)

    return render_template('predict.html', prediction=prediction) 

if __name__ == '__main__':
    app.run(debug=True)
