from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/<int:id>')
def pessoa(id ):
    return jsonify({'id':id, 'name':'Michael', 'job':'memes and dev'})

'''@app.route('/soma/<int:nun1>/<int:nun2>')
def soma( nun1, nun2):
    return jsonify({'soma': nun1 + nun2})'''

@app.route('/soma', methods=['POST'])
def soma():
    dados = json.loads(request.data)
    total = sum(dados['valores'])
    return jsonify({'soma':total})

if __name__ == "__main__":
    app.run(debug=True)