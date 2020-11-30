from flask import Flask
from flask_restful import Resource, Api, reqparse, inputs
from api_date_functions import *

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

class Days(Resource):
    def get(self, date1, date2):
        return time_between_dates(date1, date2, time_units='days')[0]

class Weeks(Resource):
    def get(self, date1, date2):
        return time_between_dates(date1, date2, time_units='days')[2]

class Weekdays(Resource):
    def get(self, date1, date2):
        return time_between_dates(date1, date2, time_units='days')[1]

api.add_resource(Days, '/days/<date1>/<date2>/')
api.add_resource(Weeks, '/weeks/<date1>/<date2>/')
api.add_resource(Weekdays, '/weekdays/<date1>/<date2>/')



if __name__ == '__main__':
    app.run(debug=True)
