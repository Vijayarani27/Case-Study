from Loan import db


# Defining Loan Model
class LoanModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    LoanType = db.Column(db.String(80), nullable=False)
    loanAmount = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.String(80), nullable=False)
    RateofInterest = db.Column(db.String(80),  nullable=False)
    DurationOfLoan = db.Column(db.String(80),  nullable=False)

    def __init__(self, LoanType, loanAmount, Date, RateofInterest, DurationOfLoan):
        self.LoanType = LoanType
        self.loanAmount = loanAmount
        self.Date = Date
        self.RateofInterest = RateofInterest
        self.DurationOfLoan = DurationOfLoan
