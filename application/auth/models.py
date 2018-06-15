from application import db
from application.models import Base

from sqlalchemy.sql import text


class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=False)

    applications = db.relationship("Application", backref='account', lazy=True)

    def __init__(self, name):
        self.name = name
        self.role = "USER"

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return self.role

    @staticmethod
    def find_users_with_no_applications():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Application ON Application.account_id = Account.id"
                    " WHERE (Application.approved IS null)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Application.id) = 0")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    @staticmethod
    def find_users_with_no_approved_applications():
        stmt = text("SELECT Account.id, Account.name FROM Account"
                    " LEFT JOIN Application ON Application.account_id = Account.id"
                    " WHERE (Application.approved != :approved OR Application.approved IS null)"
                    " GROUP BY Account.id").params(approved=True)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    @staticmethod
    def find_users_with_no_stipends():
        stmt = text("SELECT Account.id, Account.name FROM Account")
        # TODO: Täydennä siten, että hakee ne, jotka eivät stipend.receiver
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response
