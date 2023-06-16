from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    question = TextAreaField('Question')
    query = TextAreaField('Query', validators=[DataRequired()])
    submit = SubmitField('Execute')

class LoginForm(FlaskForm):
    db_type = SelectField("Database Type", choices=[("sql_server", "SQL Server"), ("mysql", "MySQL"), ("postgresql", "PostgreSQL")], validators=[DataRequired()])
    server = StringField('Server', validators=[DataRequired()])
    database = StringField('Database', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Connect')

class QuestionForm(FlaskForm):
    question = TextAreaField('Question', validators=[DataRequired()])
    query = TextAreaField('Query')
    submit = SubmitField('Submit')