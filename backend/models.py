from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db, app
from enum import Enum


class User(db.Model):
    class ProfileStatus(Enum):
        FIRST_TIME = 0
        PROFILE_COMPLETED = 1
        REPORT_COMPLETED = 2

    class BooleanStatus(Enum):
        FALSE = 0
        TRUE = 1

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    fullname = db.Column(db.String(100), index=True, unique=False)
    email = db.Column(db.String(120), index=True, unique=True)
    login_counts = db.Column(db.Integer, default=0)
    password_hash = db.Column(db.String(128))
    date_of_birth = db.Column(db.Date, nullable=True)
    blood_group = db.Column(db.Integer, nullable=True)
    marriage_status = db.Column(db.Enum(BooleanStatus), nullable=True)
    pregnancy_status = db.Column(db.Enum(BooleanStatus), nullable=True)
    no_of_abortions = db.Column(db.Integer, nullable=True)
    profile_status = db.Column(db.Enum(ProfileStatus), default=0)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_json_data(self):
        return {
            "username": self.username,
            "fullname": self.fullname,
            "email": self.email,
            "login_counts": self.login_counts,
        }

    def get_age(self):
        if self.date_of_birth:
            today = datetime.now(app.config["TIMEZONE"])
            age = (
                today.year
                - self.date_of_birth.year
                - (
                    (today.month, today.day)
                    < (self.date_of_birth.month, self.date_of_birth.day)
                )
            )
            return age
        else:
            return None


class Report(db.Model):
    class CycleStatus(Enum):
        REGULAR = 2
        IRREGULAR = 4

    class BooleanStatus(Enum):
        FALSE = 0
        TRUE = 1

    id = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    pulse_rate = db.Column(db.Integer)
    rr = db.Column(db.Integer)
    hb = db.Column(db.Float)
    cycle_status = db.Column(db.Enum(CycleStatus))
    cycle_length = db.Column(db.Integer)
    fsh = db.Column(db.Float)
    lh = db.Column(db.Float)
    hip = db.Column(db.Float)
    waist = db.Column(db.Float)
    tsh = db.Column(db.Float)
    amh = db.Column(db.Float)
    prl = db.Column(db.Float)
    vitD3 = db.Column(db.Float)
    prg = db.Column(db.Float)
    rbs = db.Column(db.Float)
    weight_gain = db.Column(db.Enum(BooleanStatus))
    hair_growth = db.Column(db.Enum(BooleanStatus))
    skin_darkening = db.Column(db.Enum(BooleanStatus))
    hair_loss = db.Column(db.Enum(BooleanStatus))
    pimples = db.Column(db.Enum(BooleanStatus))
    fast_food = db.Column(db.Enum(BooleanStatus))
    regular_exercise = db.Column(db.Enum(BooleanStatus))
    bp_systolic = db.Column(db.Integer)
    bp_diastolic = db.Column(db.Integer)
    follicle_no_l = db.Column(db.Integer)
    follicle_no_r = db.Column(db.Integer)
    avg_follicle_size_l = db.Column(db.Float)
    avg_follicle_size_r = db.Column(db.Float)
    endometrium = db.Column(db.Float)

    def get_bmi(self):
        if self.weight and self.height:
            return self.weight / (self.height * self.height)
        else:
            return None
