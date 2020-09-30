from flask_restful import Api, Resource
from flask import Flask, request
import json

list_skills = ['Python', 'R', 'JS', 'Java', 'NodeJS', 'Flask']

class SkillsFul(Resource):

    def get(self):
        return (list_skills)

    def post(self):
        data = json.loads(request.data)
        posicao = len(list_skills)
        list_skills.append(data)
        return (list_skills[posicao])

class Skills(Resource):

    def put(self, id):
        try:
            response = json.loads(request.data)
            list_skills[id] = response

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)

    def delete(self, id):
        try:
            list_skills.pop(id)
            response = {'Message':'Deletado'}

        except IndexError:
            return_mens = "Dev de ID {} não encontrado".format(id)
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)