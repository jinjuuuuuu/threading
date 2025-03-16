from flask import Flask, jsonify, make_response, abort

app = Flask(__name__)

@app.route('/api', methods=['GET']) 
def api():
    return jsonify(message="Hello, world!")

@app.route('/example/<int:id>', methods=['GET'])
def example(id):
    if id == 0:
        abort(400)
    data = {'id': id}
    response = make_response(jsonify(data))
    response.status_code = 200
    return response

if __name__ == '__main__':
    app.run(debug=True)