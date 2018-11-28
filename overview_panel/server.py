from flask_restful import Api
from flask import Flask, render_template, flash, request, jsonify, url_for, copy_current_request_context, make_response, session, redirect, abort, _request_ctx_stack
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField


# App config.
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'christy'
api = Api(app)

@app.route('/')
def index():
    """
    :return: renders index.html on page load.
     """
    return render_template("index.html")


class UserData:
    """
    Performs manipulations (save, display, delete) form inputs.
    :param self.storage : Stores all form input.
    :param self.newStore : Prevents duplicate data from getting stored.
    """
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
            flash('Channel already exists! ', 'category2')

    def get(self):
        return list(self.newStore.keys())

    def delete(self, channels):
        del self.newStore[channels]
        return list(self.newStore.keys())


p = UserData()


class ReusableForm(Form):
    """
    Declares html input field with name 'channelInput' as a text field.
    """
    channelInput = TextField('Name:', validators=[validators.required()])


@app.route("/addchannel", methods=['GET', 'POST'])
def form_data():
    """
    Uses the POST method to get the data from the form,
    performs a validation and calls the save_data instance.
    :return: renders the form in addchannel.html with the saved data.
    """

    form = ReusableForm(request.form)
    if request.method == 'POST':
        user_input = request.form['channelInput']

        if form.validate():
            p.save_data(user_input)

            flash('Channel successfully added!', 'category1')


    return render_template('addchannel.html', form=form, data=p.get())


@app.route("/removechannel", methods = ['GET','POST'])
def delete_data():
    """
     Uses the POST method to get the data from the form,
     performs a validation and calls the delete instance.
     :return:
    """

    form = ReusableForm(request.form)
    if request.method == 'POST':

        user_input = request.form['channelInput']
        if form.validate():
            p.delete(user_input)
            p.save_data(user_input)


    return {}


if __name__ == "__main__":
    app.run(port= 5000 , debug= True)