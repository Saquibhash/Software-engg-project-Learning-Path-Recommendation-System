from flask_restful import Resource, fields, marshal_with, reqparse, marshal,Api
from application.validation import NotFoundError, BusinessValidationError
from .database import db
from datetime import datetime as date,timedelta
from application.models import User,Profile,csvData,Course
import string, random
from flask_security import auth_required
from flask import abort
import base64
from flask import current_app as app
from flask import Flask, render_template,send_file,jsonify,request
from io import BytesIO
from flask import jsonify
import json
import csv
from sqlalchemy import func
from sqlalchemy import text



parse_login_user = reqparse.RequestParser()
parse_login_user.add_argument("email")
parse_login_user.add_argument("role")
parse_login_user.add_argument("password")


parse_data = reqparse.RequestParser()
parse_data.add_argument("file")

parse_profile =  reqparse.RequestParser()
parse_profile.add_argument("name")
parse_profile.add_argument("dob")
parse_profile.add_argument("email")
parse_profile.add_argument("courses")
parse_profile.add_argument("aboutMe")
parse_profile.add_argument("onlyDegree")
parse_profile.add_argument("gender")
parse_profile.add_argument("cgpa")



parse_rec = reqparse.RequestParser()
parse_rec.add_argument("domain")
parse_rec.add_argument("hours")
parse_rec.add_argument("degree")
parse_rec.add_argument("courses")





parse_rating = reqparse.RequestParser()
parse_rating.add_argument("email")
parse_rating.add_argument("subject")
parse_rating.add_argument("rating")
parse_rating.add_argument("feedback")



class UsersLoginAPI(Resource):
     def post(self):
          args = parse_login_user.parse_args()
          email = args['email']
          password = args['password']
          role = args['role']
          user= User.query.filter_by(email=email,password =password, role = role).first()
          if(user is not None):
               data={}
               if(user.role == "USER"):
                    profile_details = Profile.query.filter_by(email=email).all()
                    data["user_detail"] = [row.to_dict() for row in profile_details]
                    data["role"]= role
                    print(data)
                    return data
               if(user.role == "ADMIN"):
                    data["role"]= role
                    print(data)
                    return data
          else:
               return "invalid credentials",401
          
class DataUploadAPI(Resource):
     def put(self):
          args = parse_rating.parse_args()
          email = args['email']
          subject = args['subject']
          rating = args['rating']
          feedback = args['feedback']
          user_feedback= csvData.query.filter_by(email=email,subject = subject).first()
          user_feedback.rating = rating
          user_feedback.feedback = feedback
          db.session.commit()
          data={}
          completed_subjects = csvData.query.filter_by(email= email).all()
          data['courses'] = [row.to_dict() for row in completed_subjects]
          return data
     
     def post(self):
          args = parse_data.parse_args()
          file = args['file']
          csv_data = base64.b64decode(file).decode('utf-8')
          csv_reader = csv.reader(csv_data.splitlines())
          headers = next(csv_reader)
          for data in csv_reader:
               entry = csvData(
                     subject=data[0],level=data[1],finalGrade=data[2],score=data[3],weeklyHrs=data[4],email=data[5],feedback=data[6],rating=data[7]
                    )
               db.session.add(entry)
          db.session.commit()
          return {'message': 'CSV data successfully parsed and saved'}, 200


class UserDataUploadAPI(Resource):
     def post(self):
          print("Uploading")
          args = parse_data.parse_args()
          file = args['file']
          csv_data = base64.b64decode(file).decode('utf-8')
          csv_reader = csv.reader(csv_data.splitlines())
          headers = next(csv_reader)
          
          for data in csv_reader:
               #write in try catch block , for parsing errrors and return with error status code. 
               entry_for_profile_table = Profile(
                     name=data[0],email=data[1],level=data[2],cgpa=data[3],courses=data[4],aboutMe=data[5],onlyDegree=data[6],gender=data[7],dob=data[8]
                    )
               entry_for_user_table = User(
                     name=data[0],email=data[1],password='000',fs_uniquifier=data[1]
                    )
               # print(entry_for_user_table)
               db.session.add(entry_for_user_table)
               db.session.add(entry_for_profile_table)
          
          db.session.commit()
          return {'message': 'CSV data for user successfully parsed and saved'}, 200


class UserDataUploadAPI(Resource):
     def post(self):
          print("Uploading")
          args = parse_data.parse_args()
          file = args['file']
          csv_data = base64.b64decode(file).decode('utf-8')
          csv_reader = csv.reader(csv_data.splitlines())
          headers = next(csv_reader)
          
          for data in csv_reader:
               #write in try catch block , for parsing errrors and return with error status code. 
               entry_for_profile_table = Profile(
                     name=data[0],email=data[1],level=data[2],cgpa=data[3],courses=data[4],aboutMe=data[5],onlyDegree=data[6],gender=data[7],dob=data[8]
                    )
               entry_for_user_table = User(
                     name=data[0],email=data[1],password='000',fs_uniquifier=data[1]
                    )
               # print(entry_for_user_table)
               db.session.add(entry_for_user_table)
               db.session.add(entry_for_profile_table)
          
          db.session.commit()
          return {'message': 'CSV data for user successfully parsed and saved'}, 200
          #once successffully finished , redirect to analysis page in vue.js based on status code.
     
     def put(self):
          args = parse_rating.parse_args()
          print(args)
          input()
          email = args['email']
          # onlyDegree = args['onlyDegree']
          # print(onlyDegree)
          aboutMe = args['aboutMe']
          profile = Profile.query.filter_by(email=email).first()
          # profile.onlyDegree = onlyDegree
          profile.aboutMe = aboutMe
          db.session.commit()
          return profile

class CoursesAPI(Resource):
     def post(self):
          data = request.get_json()
          degree = data.get('degree')
          domain = data.get('domain')
          hours = data.get('hours')
          courses = data.get('courses') # loop through each course and calcualte the avg 
          count = data.get('count')
          #filter the remaining courses either in the frontend or backend based on the domain , 
          # get the avg rating and avg no of week hrs for each of the remanining subjects in the domain.
          # sort the subjects based on the rating and weekly hours.
          # select the max number of subjects with the ordering of the rating and hours.
          # if its only degree then choose priority as hrs first and then rating 
          #if else , then rating as first 
          #return all the details.
          unique_names = db.session.query(csvData.subject).distinct().all()
          unique_names = [name[0] for name in unique_names] 
          print(unique_names)
          subject_details = []
          for course in courses:
               subject_name = course['name']
               avg_rating = db.session.query(func.avg(csvData.rating)).filter(csvData.subject == subject_name).scalar()
               avg_weekly_hrs = db.session.query(func.avg(csvData.weeklyHrs)).filter(csvData.subject == subject_name).scalar()
               avg_score = db.session.query(func.avg(csvData.score)).filter(csvData.subject == subject_name).scalar()
               max_final_grade = db.session.query(func.max(csvData.finalGrade)).filter(csvData.subject == subject_name).scalar()
               #if no data is found , we can just say no results found or , just enter the data for all subjects.
               subject_details.append({
            'subject': subject_name,
            'average_rating': avg_rating,
            'average_weekly_hrs': avg_weekly_hrs,
            'level': course['level'],
            'finalGrade': max_final_grade,
            'score': avg_score,
        })
          sorted_data = sorted(subject_details, key=lambda x: (x['average_weekly_hrs'], x['average_rating']), reverse=True)
          is_degree = True
          if is_degree:
               sorted_data = sorted(sorted_data, key=lambda x: (x['average_weekly_hrs'], x['average_rating']), reverse=True)
          else:
               sorted_data = sorted(sorted_data, key=lambda x: (x['average_rating'], x['average_weekly_hrs']), reverse=True)
          if(int(count) <= len(sorted_data)):
               recommended_courses =sorted_data[:int(count)]
          else:
               recommended_courses = sorted_data
          data={}
          data['recommended_courses'] = recommended_courses
          return data
     

     def get(self,level,email):
          courses = Course.query.filter_by(level=level).all()
          data={}
          data['All_courses'] = [row.to_dict() for row in courses]
          completed_subjects = csvData.query.filter_by(level= level,email= email).all()
          data['Completed_courses'] = [row.to_dict() for row in completed_subjects]
          return data

class UserProfileAPI(Resource):

     
     def get(self,email):
          prev_Courses = csvData.query.filter_by(email=email).all()
          data={}
          data['courses']= [row.to_dict() for row in prev_Courses]
          return data
     
     def post(self):
          args = parse_profile.parse_args()
          name = args["name"]
          dob = args["dob"]
          email = args["email"]
          courses = args["courses"]
          courses_list = ','.join(courses)
          aboutme = args["aboutMe"]
          onlyDegree = args["onlyDegree"]
          gender = args["gender"]
          cgpa = args["cgpa"]
          profile_Chk = Profile.query.filter_by(email=email).first()
          print(profile_Chk)
          if profile_Chk is not None:
               profile_Chk.courses = courses_list
               profile_Chk.aboutMe = aboutme
               profile_Chk.onlyDegree = onlyDegree
               db.session.commit()
          else:
               new_profile= Profile(email=email,name=name,courses=courses_list,aboutMe=aboutme,onlyDegree=onlyDegree,gender=gender,dob=dob, cgpa = cgpa)
               db.session.add(new_profile)
               db.session.commit()
          profile_details= Profile.query.filter_by(email = email).first()
          data={}
          data['user_detail']=profile_details.to_dict()
          print(data)
          return data