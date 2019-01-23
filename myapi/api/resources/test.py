from flask_jwt_extended import jwt_required
from flask_restful import Resource


class TestResource(Resource):
    method_decorators = [jwt_required]

    def get (self):
        return {"test": "dunia ini hanya ujian"}