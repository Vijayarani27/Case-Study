import logging
from flask import request, jsonify, abort
from flask_restful import Api, Resource
from microservice import app, db
import jwt
from datetime import datetime, timedelta
from microservice.model import User, User_Loan
from microservice.schema import UserSchema
from microservice.auth import get_user
from Loan.model import LoanModel

api = Api(app)


class UserAlreadyExistsError(Exception):
    pass


errors = {
     "UserAlreadyExistsError": {
         "message": "User with given name already exists",
         "status": 400
     },
}

schema = UserSchema(many=True)
schemaone = UserSchema()


def abort_if_Id_doesnt_exist(id):
    if not User.query.get(id):
        message = "User Id {} doesn't exist".format(id)
        abort(400, message)


class UserUrl(Resource):
    def get(self):
        all_users = User.query.all()
        result = schema.dump(all_users)
        return result

    def post(self):
        error = schemaone.validate(request.json)
        if error:
            abort(400, str(error))
        try:
            id = request.json['id']
            username = request.json['username']
            password = request.json['password']
            address = request.json['address']
            state = request.json['state']
            country = request.json['country']
            pan = request.json['pan']
            contact = request.json['contact']
            dob = request.json['dob']
            accountType = request.json['accountType']
            email = request.json['email']
            user1 = User(id, username, password, address, state, country, email, contact, dob, pan, accountType)
            db.session.add(user1)
            db.session.commit()
            logging.info("Registered Successfully")
            return "Registered Successfully", 201
        except Exception:
            return errors["UserAlreadyExistsError"], 409


class UserUrlwithId(Resource):
    def get(self, id):
        user = get_user()
        abort_if_Id_doesnt_exist(id)
        if user.id != id:
            abort(403, "This is not your profile")
        user = User.query.get(id)
        user_loan = User_Loan.query.all()
        user.loan = None
        for obj in user_loan:
            if user.id == obj.user_id:
                loan = LoanModel.query.get(obj.loan_id)
                if user.loan is None:
                    user.loan = loan.LoanType
                else:
                    user.loan = user.loan+","+loan.LoanType
        db.session.commit()
        result = schemaone.dump(user)

        return result

    def put(self, id):
        user = get_user()
        abort_if_Id_doesnt_exist(id)
        if user.id != id:
            abort(403, "This is not your profile to update")
        user = User.query.get(id)
        user.id = id
        user.address = request.json['address']
        user.state = request.json['state']
        user.country = request.json['country']
        user.dob = request.json['dob']
        user.accountType = request.json['accountType']
        user.email = request.json['email']
        db.session.commit()
        logging.info("Updated Successfully")
        return "Updated Successfully"


class Login(Resource):
    def post(self):
        user = User.query.filter_by(username = request.json['username']).first()
        if not user:
            return jsonify({'Message': 'Invalid User... Please Register'})
        token = jwt.encode({
            'username': user.username,
            'exp': datetime.utcnow() + timedelta(minutes = 30)
        }, app.config['SECRET_KEY'])

        return jsonify({'token': token})


api.add_resource(UserUrl, '/userDetails')
api.add_resource(UserUrlwithId, '/userDetails/<int:id>')
api.add_resource(Login, '/login')
