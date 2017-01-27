from flask_restplus import Api

from .module_2_controller import api as ns1
from module_3.module_3_controller import api as ns2

api = Api()
api.add_namespace(ns1)
api.add_namespace(ns2)

