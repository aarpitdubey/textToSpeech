from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin

import textToSpeech

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')
          
app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try: 
        data = request.json['data']
        result = textToSpeech.textToSpeech(data)
        return {"data" : result.decode("utf-8")}
    except Exception:
        data = "you have enter an empty text.. Please enter some text, thankyou! Aap ne ek khaali vaakya diya hai Kripyaa kar ke kuch Vakyaa dijiye Dhanyaawaad"
        result = textToSpeech.textToSpeech(data)
        return {"data" : result.decode("utf-8")}

#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
     app.run(host='0.0.0.0', port=5000, debug=True)