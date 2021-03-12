import logging
from flask import request, abort
from flask_restful import Resource
from Loan import app, db
from Loan.model import LoanModel
from Loan.schema import LoanSchema
from Loan import api
from Loan.auth import get_user
from microservice.model import User_Loan, User


class UserAlreadyExistsError(Exception):
    pass


errors = {
     "UserAlreadyExistsError": {
         "message": "User with given name already exists",
         "status": 400
     },

}
loanone = LoanSchema()


class LoanwithId(Resource):
    # Getting Loan details of applied Loan by giving loan id
    def get(self, id):
        user = get_user()
        user_loan = User_Loan.query.all()
        for obj in user_loan:
            if user.id == obj.user_id and id == obj.loan_id:
                loan = LoanModel.query.get(id)
                result = loanone.dump(loan)
                return result

        return "You have not applied this loan ", 403


class Loan(Resource):
    def post(self):  # Applying Loan
        user = get_user()
        error = loanone.validate(request.json)
        if error:
            abort(400, str(error))  # Throws validation error
        id = request.json['id']
        user_loan = User_Loan.query.all()

        for obj in user_loan:
            if user.id == obj.user_id and id == obj.loan_id:
                return "You already applied this loan", 403
        LoanType = request.json['LoanType']
        loanAmount = request.json['loanAmount']
        Date = request.json['Date']
        RateofInterest = request.json['RateofInterest']
        DurationOfLoan = request.json['DurationOfLoan']

        loan1 = LoanModel(LoanType, loanAmount, Date, RateofInterest, DurationOfLoan)        
        db.session.add(loan1)
        db.session.commit()

        ul = User_Loan(user_id=user.id, loan_id=id)
        db.session.add(ul)
        db.session.commit()
        logging.info("Applied Loan")
        return "Loan Applied"


api.add_resource(Loan, '/loan')
api.add_resource(LoanwithId, '/loan/<int:id>')
