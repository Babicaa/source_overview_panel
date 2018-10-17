
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
socketio = SocketIO(app)

thread = Thread()
thread_stop_event = Event()


class ClientThread(Thread):
    def __init__(self, port, n_img, stream_host, ):
        super(ClientThread, self).__init__()
        self._delay = 1.5
        self._stream_output_port = port
        self._n_images = n_img
        self._stream_host = stream_host


if __name__== "__main__":
    socketio.run(app)
