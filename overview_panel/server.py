
# Start with a basic flask app webpage.
import csv
from string import Template
import json
import flask
from flask_socketio import SocketIO, emit
from flask_restful import Resource, Api
from flask_material import Material
from flask_cors import CORS
from flask import Flask, flash
from threading import Thread, Event
import optparse
from bsread import source
from matplotlib import pyplot, image
from flask import Flask, render_template, flash, request, jsonify, url_for, copy_current_request_context, make_response, session, redirect, abort, _request_ctx_stack
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'christy'
api = Api(app)

socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

class UserData():

    def __init__(self):
        self.storage = {}
        self.newStore = {}

    def save_data(self, channel_name):

        self.storage[channel_name]= None
        for key, value in self.storage.items():
            if key not in self.newStore.keys():
                self.newStore[key] = value
                print(self.newStore)
                break

        else:
            print('channel name already exists')

    def get(self):
        return list(self.newStore.keys())

    def delete(self):
        return



p = UserData()


class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])


@app.route("/addchannel", methods=['GET', 'POST'])
def form_data():

    form = ReusableForm(request.form)
    print(form.errors)

    if request.method == 'POST':

        user_input = request.form['name']

        if form.validate():

            p.save_data(user_input)

            flash('Channel successfully added! ')

        else:
            flash('Error: All the form fields are required. ')

    return render_template('addchannel.html', form=form , data = p.get())



if __name__ == "__main__":
    socketio.run(app)