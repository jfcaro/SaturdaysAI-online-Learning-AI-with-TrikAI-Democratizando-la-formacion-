#!/usr/bin/env python
# coding: utf-8


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField, TextAreaField, SubmitField, MultipleFileField, SelectField,RadioField
from wtforms.validators import DataRequired, Length, ValidationError, Email


class Video_playlistForm(FlaskForm):
    url = StringField ('url')
    playlist_type = SelectField("Type", choices =[("course","Course"),("documentary","Documentary"),("podcast","Podcast"),("examples","Examples")],validators=[DataRequired()])
    validate = SubmitField('validate')


class Consult(FlaskForm):
    consult = StringField('Consult', validators=[DataRequired(), Length(1, 20000)])
    level = SelectField("Level",choices=[("C","Both"),("B","Basic"),("A","Advanced")],validators=[DataRequired()])    
    validate = SubmitField('Validate')

