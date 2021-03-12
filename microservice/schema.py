from marshmallow import fields
from marshmallow.validate import Range, Length
from microservice import app,db,ma


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id", "username", "password", "address", "state", "country", "pan", "contact", "dob", "accountType", "email", "loan")
        include_fk = True

    id = fields.Integer(required=True, validate=Range(min=1))
    username = fields.Str(required=True, validate=Length(min=3))
    password = fields.Str(required=True, validate=Length(min=5))
    address = fields.Str(required=True, validate=Length(min=3))
    state = fields.Str(required=True, validate=Length(min=3))
    country = fields.Str(required=True, validate=Length(min=3))
    pan = fields.Integer(required=True, validate=Range(min=12))
    contact = fields.Integer(required=True, validate=Range(min=10))
    dob = fields.Str(required=True, validate=Length(min=5))
    accountType = fields.Str(required=True, validate=Length(min=5))
    email = fields.Str(required=True, validat=Length(min=6))
    loan = fields.Str(required=False, validate=Length(min=0))
