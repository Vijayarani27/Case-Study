from unittest import mock
from microservice import app
from microservice.model import User


def test_get_user_200():
    test = app.test_client()
    response = test.get('/userDetails')
    status = response.status_code
    assert status == 200


user = User(id=1, username='Vijay', password='password', address='Chennai', state='Tamilnadu', country='India', email='v@gmail.com', contact=8894574145, dob='21/1/1993', pan=41512563145, accountType='Saving')
test = app.test_client()


@mock.patch('microservice.view.get_user', return_value=user)
def test_get_one_user_200(mocked_object_id):
    response = test.get('/userDetails/1')
    status = response.status_code
    assert status == 200


@mock.patch('microservice.view.get_user', return_value=user)
def test_get_one_user_403(mocker):
    response = test.get('/userDetails/2')
    status = response.status_code
    assert status == 403


@mock.patch('microservice.view.get_user', return_value=user)
def test_get_one_user_400(mocker):
    response = test.get('/userDetails/8')
    status = response.status_code
    assert status == 400


user_test = {
    "username": "Kumar",
    "pan": 41512563147,
    "state": "Tamilnadu",
    "id": 3,
    "password": "pass123",
    "contact": 8894574787,
    "dob": "21/1/1986",
    "accountType": "Saving",
    "address": "Chennai",
    "country": "India",
    "email": "v6@gmail.com"
   }


@mock.patch('microservice.view.db.session.commit')  
def test_create_user_200(mocker):
    response = test.post('/userDetails', json=user_test)
    status = response.status_code
    assert status == 201


def test_create_user_400(mocker):
    user_test["username"] = ""
    response = test.post('/userDetails', json=user_test)
    status = response.status_code
    assert status == 400


def test_create_user_409(mocker):
    response = test.post('/userDetails', json={
        "username": "Vijay",
        "address": "Chennai",
        "contact": 8894574145,
        "dob": "21/1/1996",
        "state": "Tamilnadu",
        "id": 1,
        "email": "vi@gmail.com",
        "pan": 41512563145,
        "password": "password",
        "country": "India",
        "accountType": "current",
        "loan": "Car Loan,Education Loan"
    })
    status = response.status_code
    assert status == 409


@mock.patch('microservice.view.get_user', return_value=user)
def test_update_user_200(mocker_id):
    response = test.put('/userDetails/1', json={
        "state": "Tamilnadu",
        "id": 2,
        "dob": "21/1/1996",
        "accountType": "current",
        "address": "Chennai",
        "country": "India",
        "email": "vi@gmail.com"
    })
    status = response.status_code
    assert status == 200


@mock.patch('microservice.view.get_user', return_value=user)
def test_update_user_400(mocker_id):
    response = test.put('/userDetails/8', json=user_test)
    status = response.status_code
    assert status == 400


@mock.patch('microservice.view.get_user', return_value=user)
def test_update_user_403(mocker_id):
    response = test.put('/userDetails/2', json=user_test)
    status = response.status_code
    assert status == 403


def test_login_200():
    response = test.post('/login', json={"username": "Vijay", "password": "password"})
    status = response.status_code
    assert status == 200
