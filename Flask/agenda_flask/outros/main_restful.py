from flask import Flask, request
from flask_restful import Api, Resource
import json
from skills import Skills, SkillsFul

app = Flask(__name__)
api = Api(app)

list_devs = [{'id': 0, 'name':'michael', 'skills': ["python", 'R']},
             {'id': 1,'name':'Uewerton', 'skills': ["Java", 'JS']}]

class Dev(Resource):
    
    def get(self, id):      
        try:
            response =  list_devs[id]

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        except Exception:
            return_mens = "Erro desconhecido"
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)

    def put(self, id):
        try:
            response = json.loads(request.data)
            list_devs[id] = response

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)

    def delete(self, id):
        try:
            list_devs.pop(id)
            response = {'Message':'Deletado'}

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)

class DevFul(Resource):

    def get(self):
        return (list_devs)

    def post(self):
        data = json.loads(request.data)
        posicao = len(list_devs)
        data['id'] = posicao
        list_devs.append(data)
        return (list_devs[posicao])


api.add_resource(DevFul, '/dev/')
api.add_resource(Dev, '/dev/<int:id>')
api.add_resource(SkillsFul, '/skills/')
api.add_resource(Skills, '/skills/<int:id>')


if __name__ == "__main__":
    app.run()