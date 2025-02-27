from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
  #Flask 객체 인스턴스 생성
  app = Flask(__name__)
  CORS(app, resources={r'*': {'origins': '*'}})
  # .env 파일 만들어서 gitignore에 등록 후 중요 정보들 불러오기
  app.config["SQLALCHEMY_DATABASE_URI"] = "." 
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  app.config['SECRET_KEY'] = "dev1234"
  app.config['JSON_AS_ASCII'] = False
  
  db.init_app(app)
  migrate = Migrate(app, db)
  migrate.init_app(app, db)
  
  from model import models

  from route import login_route, content_route, random_route, like_route, dislike_route, register_route, survey_route, logout_route, mypage_route, filter_route, reviews_route
  
  app.register_blueprint(login_route.bp)
  app.register_blueprint(content_route.bp)
  app.register_blueprint(random_route.bp)
  app.register_blueprint(like_route.bp)
  app.register_blueprint(dislike_route.bp)
  app.register_blueprint(register_route.bp)
  app.register_blueprint(survey_route.bp)
  app.register_blueprint(logout_route.bp)
  app.register_blueprint(mypage_route.bp)
  app.register_blueprint(filter_route.bp)
  app.register_blueprint(reviews_route.bp)
  return app
