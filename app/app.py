from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)

# app.config.from_pyfile('config.cfg')
app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.app_context().push()

db = SQLAlchemy()
db.init_app(app)


class Client(db.Model):
    __tablename__ = 'clients'

    # Fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    money = db.Column(db.Integer)

    # Initialize database
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __repr__(self):
        return '<id {}>'.format(self.id)

    # For JSON serialization purposes
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'money': self.money
        }


# Index

@app.route("/")
def index():
    return "This is the app index"


# Test/create db

@app.route('/init_db')
def test_db():
    db.create_all()
    db.session.commit()
    # c = Client(name='test', money='1')
    client = Client.query.first()
    # return "Database initialized with '{} {}' ".format(c.name, c.money)
    c = Client(name='test', money='1')
    if not client:
        db.session.add(c)
        db.session.commit()
        Client.query.first()
    return "Client '{} {}' is from database".format(c.name, c.money)


# Add client and money


@app.route("/add")
def add_client():
    name = request.args.get('name')
    money = request.args.get('money')
    try:
        c = Client(
            name=name,
            money=money
        )
        db.session.add(c)
        db.session.commit()
        return "Client added with id={}".format(c.id)
    except Exception as e:
        return str(e)


# Get all clients


@app.route("/getall")
def get_all():
    try:
        clients = Client.query.all()
        return jsonify([e.serialize() for e in clients])
    except Exception as e:
        return str(e)


# Get client by ID


@app.route("/get/<id_>")
def get_by_id(id_):
    try:
        client = Client.query.filter_by(id=id_).first()
        return jsonify(client.serialize())
    except Exception as e:
        return str(e)


# Get client by Name


@app.route("/getn/<name_>")
def get_by_name(name_):
    try:
        client = Client.query.filter_by(name=name_).first()
        return jsonify(client.serialize())
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
