import io
from flask import Flask,request, jsonify,render_template_string
from flask_cors import CORS
import pyshorteners
import segno

app = Flask(__name__)
CORS(app)

def QR_code_gen(tiny_url_to_qr_code):
    qr = segno.make(tiny_url_to_qr_code)
    buff = io.BytesIO()
    return qr.save(buff, kind='svg')


@app.route('/', methods=['GET'])
def ops():
    return jsonify(status=405, response="ops!... can you try send me an json request with input_url as key of your input", for_admin="with all of our ❤ #NeverStopLarning",)

@app.route('/qr-generator', methods=['GET', 'POST'])
def question():
    shortener = pyshorteners.Shortener()
    request_data = request.get_json()   

    if request_data:
        if 'input_url' in request_data:
            raw_url = request_data['input_url']
            input_url= render_template_string(raw_url)
            tiny_url = shortener.tinyurl.short(input_url)

    return jsonify(old_url=input_url,tiny_url=tiny_url, qr_code=QR_code_gen(tiny_url), status=200)

if __name__ == '__main__':
    app.run(debug=True, port=5000)