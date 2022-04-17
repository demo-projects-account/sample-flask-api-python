from flask import Flask, jsonify

app = Flask(__name__)

items = [
    {
        'name': 'Table',
        'price': 5000
    },
    {
        'name': 'Chair',
        'price': 3000
    }
]


@app.route('/')
def index():
    # return {'message': 'Working fine..'}
    return jsonify(message='Working fine...')


@app.route('/items')
def fetch_items():
    return jsonify(items=items)


#if __name__ == '__main__':
   # app.run(host='0.0.0.0', debug=False)
 
from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
