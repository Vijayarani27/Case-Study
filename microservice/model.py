from microservice import app,db,ma


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80),  nullable=False)
    country = db.Column(db.String(80),  nullable=False)
    pan = db.Column(db.Integer, unique=True, nullable=False)
    contact = db.Column(db.Integer, unique=True, nullable=False)
    dob = db.Column(db.String, nullable=False)
    accountType = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    loan = db.Column(db.String(120), nullable=True)
    # loan_id = db.Column(db.Integer, db.ForeignKey("loan_model.id"))
    # loan = db.relationship("LoanModel", backref="loan_model",primaryjoin="LoanModel.id == User.loan_id")

    def __repr__(self):
        return '<User %r>' % self.username

    def __init__(self, id, username, password, address, state, country, email, contact, dob, pan, accountType):
        self.id = id
        self.username = username
        self.password = password
        self.address = address
        self.state = state
        self.country = country
        self.pan = pan
        self.contact = contact
        self.dob = dob
        self.accountType = accountType
        self.email = email


class User_Loan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    loan_id = db.Column(db.Integer, nullable=False)
