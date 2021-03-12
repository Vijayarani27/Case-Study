from marshmallow import fields
from marshmallow.validate import Range, Length
from Loan import ma


# Defining Schema for Loan Model
class LoanSchema(ma.SQLAlchemySchema):
    class Meta:
        fields = ("id", "LoanType", "loanAmount", "Date", "RateofInterest",
                  "DurationOfLoan")
        include_fk = True

    id = fields.Integer(required=True, validate=Range(min=1))
    LoanType = fields.Str(required=True, validate=Length(min=3))
    loanAmount = fields.Integer(required=True, validate=Range(min=10000))
    Date = fields.Str(required=True, validate=Length(min=3))
    RateofInterest = fields.Str(required=True, validate=Length(min=3))
    DurationOfLoan = fields.Integer(required=True, validate=Range(min=1))
