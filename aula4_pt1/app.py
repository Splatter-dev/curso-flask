from flask import Flask

import views



def create_app():
    """Factory principal"""

    app = Flask(__name__)
    views.init_app(app)

    return app


# # forma antiga de rodar o app
# if __name__ == '__main__':
#     app =  create_app()
#     app.run()

# gambiarra para não cair no circular import
# app = Flask(__name__)
# from views import index, contato
