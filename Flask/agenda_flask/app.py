from flask import Flask, request
from flask_restful import Api, Resource
import json
import models

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):

    def get(self, nome):
        
        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        try:

            response = {
                'nome':pessoa.nome,
                'idade':pessoa.idade,
                'id':pessoa.id
            }

        except AttributeError:
            return_mens = "Pessoa com nome: {} não foi encontrado(a)".format(nome)
            response = {'status':'erro', 'mensagem': return_mens}

        except Exception:
            return_mens = "Erro desconhecido"
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)


    def put(self, nome):

        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        try:
            dados = request.json

            if 'nome' in dados: pessoa.nome = dados['nome']
            if 'idade' in dados: pessoa.idade = dados['idade'] 
            pessoa.save()

            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }

        except AttributeError:
            return_mens = "Pessoa com nome: {} não foi encontrado(a)".format(nome)
            response = {'status':'erro', 'mensagem': return_mens}

        except Exception:
            return_mens = "Erro desconhecido"
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)


    def delete(self, nome):
        
        pessoa = models.Pessoas.query.filter_by(nome=nome).first()
        try:
            pessoa.delete()
            response = {'Status':'Sucessp','Message':'Pessoa {} Deletado(a)'.format(pessoa.nome)}

        except AttributeError:
            return_mens = "Pessoa com nome: {} não encontrado(a)".format(nome)
            response = {'status':'erro', 'mensagem': return_mens}

        return (response)

class Pessoas(Resource):

    def get(self):

        pessoas = models.Pessoas.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas ]
        return (response)


    def post(self):

        dados = request.json
        pessoa = models.Pessoas(nome=dados['nome'],idade=dados['idade'])
        pessoa.save()

        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade 
        }
        return (response)


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Pessoas, '/pessoa/')

if __name__ == '__main__':
    app.run(debug=True)