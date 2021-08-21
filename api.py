from analytic import analyze
from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Trigger(Resource):
    @staticmethod
    def get():
        return {'status': 'connected'}

    def post(self):
        current_session_id = request.args.get('sessionId')
        if current_session_id == '' or current_session_id == '0':
            return {}

        analyze.predict(session_id=current_session_id)

        return {}


api.add_resource(Trigger, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
