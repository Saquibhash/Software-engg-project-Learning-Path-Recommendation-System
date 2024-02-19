import os
from flask import Flask
from flask_restful import Resource,Api
from flask_cors import CORS
from application import config
from application.config import LocalDevelopmentConfig
from application.database import db
from application.models import User, Role
from flask_security import Security, SQLAlchemyUserDatastore
import redis


app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "ticketshow"
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)


    app.app_context().push()

    api = Api(app)
    app.app_context().push()

    CORS(app, supports_credentials=True)
    app.config['CORS_HEADERS'] = 'application/json'

    return app, api

app, api = create_app()

from application.controllers import *
from application.api import *


api.add_resource(UsersLoginAPI,"/user/login")
api.add_resource(DataUploadAPI,"/admin/uploadData","/user/rating")
api.add_resource(UserDataUploadAPI,"/admin/userData", "/user/updateProfile")
api.add_resource(UserProfileAPI,"/user/submitProfileDetails","/user/courses/<email>")
api.add_resource(CoursesAPI,"/courses/<level>/<email>","/user/generateRecommendation")


if __name__ == '__main__':
  app.run(host='0.0.0.0',port=8080)
