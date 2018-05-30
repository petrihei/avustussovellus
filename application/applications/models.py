from application import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    sum = db.Column(db.Integer, nullable=False)
    definition = db.Column(db.String(1000), nullable=False)
    approved = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                            nullable=False)

    def __init__(self, name):
        self.name = name
        self.sum = 0
        self.definition = ""
        self.approved = False
