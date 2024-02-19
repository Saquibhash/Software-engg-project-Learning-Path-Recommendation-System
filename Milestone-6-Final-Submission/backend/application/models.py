from .database import db
from flask_security import UserMixin, RoleMixin



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    fs_uniquifier = db.Column(db.String, unique=True, nullable=False)
    role = db.Column(db.String,default='USER')
    def to_dict(self):
        data = {
            'name': self.name,
            'email': self.email,
            'role': self.role
        } 
        return data

roles_users = db.Table('roles_users', 
                db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
                db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Profile(db.Model):
    __tablename__ = 'profileDetails'
    email = db.Column(db.String,nullable=False,primary_key=True)#it should be non editable.
    name = db.Column(db.String,nullable=False)#it should be non editable.
    level = db.Column(db.String, nullable = False)
    cgpa = db.Column(db.String,nullable = False)
    courses = db.Column(db.String,nullable=False)
    aboutMe = db.Column(db.String,nullable=False)
    onlyDegree = db.Column(db.String,nullable=False)
    gender = db.Column(db.String,nullable=False)
    dob = db.Column(db.String,nullable=False) #write foreign key r/p to other tables from Database.

    def to_dict(self):
        data = {
            'email': self.email,
            'name'  : self.name,
            'level':self.level,
            'cgpa':self.cgpa,
            'courses':self.courses,
            'aboutMe': self.aboutMe,
            # 'experience': self.experience,
            'onlyDegree': self.onlyDegree,
            'gender': self.gender,
            'dob': self.dob,
        } 
        return data

class Course(db.Model):
    __tablename__ = 'course'
    name = db.Column(db.String,nullable=False,primary_key=True)#it should be non editable.
    level = db.Column(db.String,nullable=False)
    faculty = db.Column(db.String,nullable=False)
    category = db.Column(db.String,nullable=False)

    def to_dict(self):
        data = {
            'name'  : self.name,
            'level': self.level,
            'faculty': self.faculty,
            'category': self.category,
        } 
        return data

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course = db.Column(db.String,nullable=False,primary_key=True)#it should be non editable.
    rating = db.Column(db.String,nullable=False)
    review = db.Column(db.String,nullable=False)#write foreign key r/p to other tables from Database.

    def to_dict(self):
        data = {
            'course'  : self.course,
            'rating': self.rating,
            'review': self.review,
        } 
        return data


class csvData(db.Model):
    __tablename__ = 'csvData'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String,nullable=False)
    subject = db.Column(db.String,nullable=False)
    level = db.Column(db.String,nullable=False)
    finalGrade = db.Column(db.String,nullable=False)
    weeklyHrs = db.Column(db.Integer,nullable=False)
    score = db.Column(db.Integer,nullable=False)
    feedback = db.Column(db.String,nullable=False)
    rating = db.Column(db.Integer,nullable=False)

    def to_dict(self):
        data = {
            'email':self.email,
            'subject': self.subject,
            'level': self.level,
            'finalGrade': self.finalGrade,
            'weeklyHrs': self.weeklyHrs,
            'score':self.score,
            'feedback':self.feedback,
            'rating': self.rating,
        } 
        return data