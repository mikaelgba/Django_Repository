from flask import request
import models
import json

def get_pessoa(self, nome):
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


def alterar_dados_pessoa(self, nome):
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

def deletar_pessoa(self, nome):
    pessoa = models.Pessoas.query.filter_by(nome=nome).first()
    try:
        pessoa.delete()
        response = {'Status':'Sucesso','Message':'Pessoa {} Deletado(a)'.format(pessoa.nome)}

    except AttributeError:
        return_mens = "Pessoa com nome: {} não encontrado(a)".format(nome)
        response = {'status':'erro', 'mensagem': return_mens}

    return (response)

def get_todas_pessoas(self):
    pessoas = models.Pessoas.query.all()
    response = [{'id':i.id, 'nome':i.nome, 'idade':i.idade} for i in pessoas ]
    return (response)

def add_pessoa(self):
    dados = request.json
    pessoa = models.Pessoas(nome=dados['nome'],idade=dados['idade'])
    pessoa.save()

    response = {
        'id':pessoa.id,
        'nome':pessoa.nome,
        'idade':pessoa.idade 
    }
    return (response)

def get_todas_atividades(self):
    atividades = models.Atividades.query.all()
    response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades]
    return (response)

def add_atividade(self):
    dados = request.json
    pessoa = models.Pessoas.query.filter_by(nome=dados['pessoa']).first()
    atividade = models.Atividades(nome=dados['nome'], pessoa=pessoa)
    atividade.save()

    response = {
        'id':atividade.id,
        'nome':atividade.nome,
        'pessoa':atividade.pessoa.nome
    }
    return (response)