from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource,reqparse,abort

app=Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class VideoModel(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    views=db.Column(db.Integer,nullable=False)
    likes=db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f'Video(name{name},views={views},likes={likes}'

video_put_args=reqparse.RequestParser()

video_put_args.add_argument("name",type=str,help="Name of the video is required",required=True)
video_put_args.add_argument("views",type=int,help="Views of the video is required",required=True)
video_put_args.add_argument("likes",type=int,help="Likes on the video is required",required=True)


class Video(Resource):
    def get(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id]

    def put(self,video_id):
        abort_if_video_exists(video_id)
        args=video_put_args.parse_args()
        videos[video_id]=args
        return videos[video_id], 201

    def delete(self,video_id):
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return '',204


api.add_resource(Video,'/video/<int:video_id>')


if __name__=='__main__':
    app.run(debug=True)