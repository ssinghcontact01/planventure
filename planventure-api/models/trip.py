from datetime import datetime, timezone
from app import db

class Trip(db.Model):
    __tablename__ = 'trips'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    destination = db.Column(db.String(255), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    itinerary = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    
    # Relationship to User
    user = db.relationship('User', backref=db.backref('trips', lazy=True, cascade='all, delete-orphan'))
    
    def to_dict(self):
        """Convert trip object to dictionary"""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'destination': self.destination,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'coordinates': {
                'latitude': self.latitude,
                'longitude': self.longitude
            },
            'itinerary': self.itinerary,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    def __repr__(self):
        return f'<Trip {self.destination}>'
