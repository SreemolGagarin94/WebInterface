from WebInterface import db


class Users(db.Model):
    id=db.Column(db.Integer(),db.Identity(start=1),primary_key=True)
    name = db.Column(db.String(length=50),nullable=False)
    username=db.Column(db.String(length=50),unique=True,nullable=False)
    password = db.Column(db.String(length=20),nullable = False)

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return str(self.id)