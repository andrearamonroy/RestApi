#modules 
from email import message
from flask import Flask
from flask_restful import Api, Resource, abort, reqparse, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)  #wraps the app in an restful api
#changing the configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app) #wraps the app in a db 

#create the model before you create the db
class FrenchModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

  



#creating the database only once bc if I run it again it will reinitialize and overwrite the tables and data in the db
#db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="error: name of vid")
video_put_args.add_argument("views", type=str, help="error: views of vid")
video_put_args.add_argument("likes", type=str, help="error: likes of vid")

""" levels =  {}

def abort_if_level_id_doesnt_exist(video_id):
    if video_id not in levels:
        abort(404, message= "Could not find video")

#if it already exists
def abort_if_video_exists(video_id):
    if video_id in levels:
        abort(409, message= "Video already exists in levels") """

class French(Resource):
    def get(self, video_id):
        return levels[video_id]

#create
    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_put_args.parse_args()
        levels[video_id] = args
        return levels[video_id], 201




#class inherits from resource so it means that this class is a resource, that handles methods such as CRUD
#class FrenchLevels(Resource):
#    def get(self):
#       return levels

api.add_resource(French,"/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)

