#!/usr/bin/env python
"""Database initialization script to create all tables."""

from app import app, db
from models import User

def init_db():
    """Initialize the database by creating all tables."""
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("✓ Database tables created successfully!")
        print("Tables created:")
        print("  - users")

if __name__ == '__main__':
    init_db()
