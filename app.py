from flask import Flask, jsonify
from news import get_news
from service import get_service
from status import get_status
from traffic import get_traffic

app = Flask(__name__)

@app.route('/news')
def news():
    return jsonify(get_news())

@app.route('/service')
def service():
    return jsonify(get_service())

@app.route('/status')
def status():
    return jsonify(get_status())

@app.route('/traffic')
def traffic():
    return jsonify(get_traffic())

if __name__ == '__main__':
    app.run(debug=True)
