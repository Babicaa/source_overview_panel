
# Start with a basic flask app webpage.
from flask_socketio import SocketIO, emit
from flask_restful import Resource, Api
from flask_material import Material
from flask_cors import CORS
from flask import Flask, flash, jsonify, render_template, url_for, copy_current_request_context, request, make_response, session, redirect, abort, _request_ctx_stack
from threading import Thread, Event
import optparse
from bsread import source
from matplotlib import pyplot, image

__author__ = 'christy'

app = Flask(__name__)
Material(app)
CORS(app)

api = Api(app)
app.config['SECRET_KEY'] = 'christy'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)