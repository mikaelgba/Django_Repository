from flask import Flask, request
from flask_restful import Api, Resource
from flask_httpauth import HTTPBasicAuth
import servicos

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

@auth.verify_password
def verificacao(login, senha):

    if not (login, senha):
        return False
    return servicos.models.Usuarios.query.filter_by(login=login, senha=senha).first()

class Pessoa(Resource):

    @auth.login_required
    def get(self, nome):        
        response = servicos.get_pessoa(self, nome)
        return (response)

    @auth.login_required
    def put(self, nome):
        response = servicos.alterar_dados_pessoa(self, nome)
        return (response)

    @auth.login_required
    def delete(self, nome):       
        response = servicos.deletar_pessoa(self, nome)
        return (response)

class Pessoas(Resource):
    
    @auth.login_required
    def get(self):
        response = servicos.get_todas_pessoas(self)
        return (response)

    def post(self):
        response = servicos.add_pessoa(self)
        return (response)

class Atividades(Resource):

    @auth.login_required
    def get(self):
        response = servicos.get_todas_atividades(self)
        return (response)

    def post(self):
        response = servicos.add_atividade(self)
        return (response)


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(Pessoas, '/pessoa/')
api.add_resource(Atividades, '/atividade/')

if __name__ == '__main__':
    app.run(debug=True)