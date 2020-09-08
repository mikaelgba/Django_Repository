from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
'''videos_db.create_all()'''

data_video_put_args = reqparse.RequestParser()
data_video_put_args.add_argument("name", type=str, help="Name of video", required=True)
data_video_put_args.add_argument("link", type=str, help="link of video", required=True)
data_video_put_args.add_argument("views", type=int, help="views of video", required=True)
data_video_put_args.add_argument("likes", type=int, help="likes on video", required=True)

class VideoModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    link = db.Column(db.String(400), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__ (self):
        return f"Video(name={name}, link={link}, views={views}, likes={likes})"

resource_fields = {'id': fields.Integer, 'name': fields.String, 'link': fields.String, 'views': fields.Integer, 'likes': fields.Integer}

db.create_all()

class Video(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = data_video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args['name'], link=args['link'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)