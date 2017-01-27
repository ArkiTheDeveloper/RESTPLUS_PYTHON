from flask import Flask

from module_2 import api as mod_1

app = Flask(__name__)
mod_1.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

