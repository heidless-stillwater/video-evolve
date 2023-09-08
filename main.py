from flask import Flask, render_template, request
from flask_restful import Api, Resource, reqparse, abort
import datetime

# importing the math library
import math

app = Flask(__name__)
api = Api(app)

@app.route('/test')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

class HelloWorld(Resource):
  def get(self, name, age):
 #   return {"data": "Hello World"}
 #   test = test*10
    age_seconds = age*31536000
    #lifetimes = age * 2**age
    # calculating the log2(number)
    lifetimes = math.log2(age_seconds)
    # displaying the result
    #print(f"The logarithm of base 2, of {number} is = {result}")
    return {"name": name, "age": age, "age_seconds": age_seconds, "lifetimes": lifetimes}
  
  def post(self):
    return {"data": "posted"}

api.add_resource(HelloWorld, '/helloworld/<string:name>/<int:age>')

names = {
  "tim":  {"age":19, "gender":"male"},
  "bill": {"age":58, "gender":"female"}
}

class Name(Resource):
  def get(self, name):
    return names[name]

api.add_resource(Name, '/name/<string:name>')

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of Video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Num Likes is required", required=True)
video_put_args.add_argument("views", type=int, help="Num Views id required", required=True)

videos = {}

def abort_if_video_id_doesnt_exist(video_id):
  if video_id not in videos:
    abort(404, message="Video does not exist...")

def abort_if_video_id_exists(video_id):
  if video_id in videos:
    abort(409, message="Video exists...")

class Video(Resource):
  def get(self, video_id):
    abort_if_video_id_doesnt_exist(video_id)
    return videos[video_id]
  
  def put(self, video_id):
    abort_if_video_id_exists(video_id)
    args = video_put_args.parse_args()
    videos[video_id] = args
    return videos[video_id], 201
  
  def delete(self, video_id):
    abort_if_video_id_doesnt_exist(video_id)
    del videos[video_id]
    return '', 204    
    
    
    

api.add_resource(Video, '/video/<int:video_id>')
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
  
  
