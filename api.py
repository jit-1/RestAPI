from flask import Flask 
from flask_restful  import Resources, Api

app = Flask(__name__)
api=Api(app)