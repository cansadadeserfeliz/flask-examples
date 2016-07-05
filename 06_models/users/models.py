from ..run import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    city_id = db.Column(db.ForeignKey(u'cities.id'), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(),
                        onupdate=db.func.now())

    def __repr__(self):
        return '<Usuario %r>' % self.username


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    drivers = db.relationship('User', backref='city', lazy='dynamic')
