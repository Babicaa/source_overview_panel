
# Start with a basic flask app webpage.
from string import Template

from flask_socketio import SocketIO, emit
from flask_restful import Resource, Api
from flask_material import Material
from flask_cors import CORS
from flask import Flask, flash, jsonify, render_template, url_for, copy_current_request_context, request, make_response, session, redirect, abort, _request_ctx_stack
from threading import Thread, Event
import optparse
from bsread import source
from matplotlib import pyplot, image
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'christy'

socketio = SocketIO(app)

global store
store = {}

@app.route('/')
def index():
    return render_template("index.html")




class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

@app.route("/addchannel", methods=['GET', 'POST'])
def form_data():

    global store
    form = ReusableForm(request.form)
    print(form.errors)

    if request.method == 'POST':
        name = request.form['name']
        store = {'key': name}
        print(store)


        if form.validate():

            flash('Channel successfully added! ')
        else:
            flash('Error: All the form fields are required. ')

    return render_template('addchannel.html', form=form, store=store)







if __name__ == "__main__":
    socketio.run(app)