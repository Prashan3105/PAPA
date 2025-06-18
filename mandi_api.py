
from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import get_mandi_data

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "🌾 Mandi Bhav API Running"

@app.route('/mandi', methods=['GET'])
def mandi_bhav():
    state = request.args.get('state')
    district = request.args.get('district')
    data = get_mandi_data(state, district)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
