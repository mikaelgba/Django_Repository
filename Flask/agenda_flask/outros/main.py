from flask import Flask, jsonify, request
import json

app = Flask(__name__)

list_devs = [{'id': 0, 'name':'michael', 'skills': ["python", 'R']},
             {'id': 1,'name':'Uewerton', 'skills': ["Java", 'JS']}]

@app.route('/dev/<int:id>', methods=['GET','PUT','DELETE','POST'])
def dev(id):

    if(request.method == 'GET'):
        try:
            response =  list_devs[id]

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        except Exception:
            return_mens = "Erro desconhecido"
            response = {'status':'erro', 'mensagem': return_mens}
        return jsonify(response)


    elif(request.method == 'PUT'):

        try:
            response = json.loads(request.data)
            list_devs[id] = response

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        return jsonify(response)


    elif(request.method == 'DELETE'):

        try:
            list_devs.pop(id)
            return jsonify({'Message':'Deletado'})

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}
            return jsonify(response)

@app.route('/dev/', methods=['GET','POST'])
def dev_full():

    if(request.method == 'GET'):
        return jsonify(list_devs)

    elif(request.method == 'POST'):
        data = json.loads(request.data)
        posicao = len(list_devs)
        data['id'] = posicao
        list_devs.append(data)
        return jsonify(list_devs[posicao])

if __name__ == "__main__":
    app.run(debug=True)