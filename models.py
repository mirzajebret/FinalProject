from datetime import datetime
from config import db, ma

class Wish(db.Model):
    __table_args__ = {'extend_existing': True}
    __tablename__ = 'wish'
    wish_id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String(255))
    title = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class WishSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wish
        sqla_session = db.session    