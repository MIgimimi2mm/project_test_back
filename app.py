from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS設定を追加

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/message', methods=['POST'])
def process_message():
    data = request.get_json()
    input_text = data['inputText']
    modified_message = input_text + 'だみょ～ん'
    return jsonify({'message': modified_message})

if __name__ == '__main__':
    app.run(debug=True)