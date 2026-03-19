from datetime import datetime, timezone
from app import db
from bcrypt import hashpw, gensalt, checkpw

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)
    
    def set_password(self, password):
        """Hash and set the password"""
        self.password_hash = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
    
    def check_password(self, password):
        """Verify password against stored hash"""
        return checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
    
    # Add relationship to trips
    trips = db.relationship('Trip', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<User {self.email}>'
