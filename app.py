from flask import Flask,request, jsonify,render_template_string
import pyshorteners
import pyqrcode

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ops():
    return jsonify(response="ops!... can you try send me an json request with input_url as key of your input", for_admin="with all of our ❤ #NeverStopLarning")

@app.route('/qr-generator', methods=['GET', 'POST'])
def question():
    shortener = pyshorteners.Shortener()
    request_data = request.get_json()   

    if request_data:
        if 'input_url' in request_data:
            raw_url = request_data['input_url']
            input_url= render_template_string(raw_url)

            tiny_url = shortener.tinyurl.short(input_url)
            # qr_code = pyqrcode.create(tiny_link)
        
    return jsonify(old_url=input_url,tiny_link=tiny_url)

if __name__ == '__main__':
    app.run(debug=True, port=5000)