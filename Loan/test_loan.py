from unittest import mock
from Loan.model import *
from Loan.auth import *
from microservice.model import User
from Loan import app

user = User(id=1, username='Vijay', password='password', address='Chennai', state='Tamilnadu', country='India', email='v@gmail.com', contact=8894574145, dob='21/1/1993', pan=41512563145, accountType='Saving')
test = app.test_client()


@mock.patch('Loan.view.get_user', return_value=user)
def test_get_appliedLoan_200(mocked_object_id):
    response = test.get('/loan/1')
    status = response.status_code
    assert status == 200


@mock.patch('Loan.view.get_user', return_value=user)
def test_get_appliedLoan_403(mocked_object_id):
    response = test.get('/loan/4')
    status = response.status_code
    assert status == 403


loan = {
    "LoanType": "Car Loan",
    "loanAmount": 500000,
    "Date": "21/1/2020",
    "RateofInterest": "2%.",
    "id": 1,
    "DurationOfLoan": 3
}


@mock.patch('Loan.view.get_user', return_value=user)
def test_apply_Loan_403(mocked_object_id):
    response = test.post('/loan', json=loan)
    status = response.status_code
    assert status == 403


@mock.patch('Loan.view.get_user', return_value=user)
def test_apply_Loan_400(mocked_object_id):
    loan["LoanType"] = ""
    response = test.post('/loan', json=loan)
    status = response.status_code
    assert status == 400
