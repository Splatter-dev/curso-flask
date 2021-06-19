#forma com circular import
# from app import app

"""Extensão Flask"""
from flask import Flask, request


def init_app(app: Flask):
    """Inicialização de extensões"""

    @app.route("/")
    def index():
        print(request.environ['HTTP_USER_AGENT'])
        return "Esta rodando aguarde"

    @app.route("/contato")
    def contato():
        return "<form><input type='text'></input></form>"

## em poo 
# class Views:

#     def init_app(self, app: Flask):    

#         @app.route("/")
#         def index():
#             print(request.environ['HTTP_USER_AGENT'])
#             return "Esta rodando aguarde"

#         @app.route("/contato")
#         def contato():
#             return "<form><input type='text'></input></form>"

# forma com cirular import
# @app.route('/')
# def index():
#     return f'Hello World'

# @app.route('/contato')
# def contato():
#     return f'<form><input type="text"></form></input>'