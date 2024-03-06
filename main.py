from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from wtforms import EmailField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, Email
from wtforms.validators import Email
from mailing import send_email
import os
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY_APP']
Bootstrap5(app)


class ContactForm(FlaskForm):
    email_number = StringField('Subject', validators=[DataRequired()])
    message = CKEditorField('Message', validators=[DataRequired()])
    submit = SubmitField('Contact Me')


@app.route('/')
def home():
    return render_template('index.html',
                           age=int((date.today() - date(2000, 4, 23)).days / 365))


@app.route('/gallery')
def gallery():
    urls = [url_for('static', filename=f"img_gallery/{file}") for file in os.listdir('./static/img_gallery')]
    return render_template('gallery.html', imgs=urls)


@app.route('/about_contact', methods=['GET', 'POST'])
def about_contact():
    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        send_email(email="cujo.kuzin@gmail.com",
                   contact_email=contact_form.data['email_number'],
                   message=contact_form.data['message'])
        return redirect(url_for('about_contact'))
    return render_template('about_contact.html', form=contact_form)


if __name__ == "__main__":
    app.run(debug=True)