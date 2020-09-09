from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
videos_db = SQLAlchemy(app)
'''videos_db.create_all()'''

# para add, recebe os dados para o put
data_video_put_args = reqparse.RequestParser()
data_video_put_args.add_argument("name", type=str, help="Name of video", required=True)
data_video_put_args.add_argument("link", type=str, help="link of video", required=True)
data_video_put_args.add_argument("views", type=int, help="views of video", required=True)
data_video_put_args.add_argument("likes", type=int, help="likes on video", required=True)

# para up, recebe os dados para o patch
data_video_up_args = reqparse.RequestParser()
data_video_up_args.add_argument("name", type=str, help="Name of video")
data_video_up_args.add_argument("link", type=str, help="link of video")
data_video_up_args.add_argument("views", type=int, help="views of video")
data_video_up_args.add_argument("likes", type=int, help="likes on video")

class VideoModel(videos_db.Model):

    id = videos_db.Column(videos_db.Integer, primary_key=True)
    name = videos_db.Column(videos_db.String(120), nullable=False)
    link = videos_db.Column(videos_db.String(400), nullable=False)
    views = videos_db.Column(videos_db.Integer, nullable=False)
    likes = videos_db.Column(videos_db.Integer, nullable=False)

    def __repr__ (self):
        return f"Video(name={name}, link={link}, views={views}, likes={likes})"

resource_fields = {'id': fields.Integer, 'name': fields.String, 'link': fields.String, 'views': fields.Integer, 'likes': fields.Integer}

videos_db.create_all()

class Video(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if (not result): return abort(404, message="Não foi encontrado video com este ID")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = data_video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if (result): return abort(409, message="ID já foi cadastrado em um video")

        video = VideoModel(id=video_id, name=args['name'], link=args['link'], views=args['views'], likes=args['likes'])
        videos_db.session.add(video)
        videos_db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = data_video_up_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()

        if (not result): return abort(404, message="Não encontrado")

        if (args['name']): result.name = args['name']
        if (args['link']): result.link = args['link']
        if (args['views']): result.views = args['views']
        if (args['likes']): result.likes = args['likes']

        videos_db.session.commit()
        return result

    @marshal_with(resource_fields)
    def delete(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()

        if (not video): return abort(404, message="Não foi encontrado")
        videos_db.session.delete(video)
        videos_db.session.commit()
        return "Deletado", 204

class Video_full(Resource):

    @marshal_with(resource_fields)
    def get(self):
        videos = VideoModel.query.order_by().all()
        return videos

api.add_resource(Video_full, "/video")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)