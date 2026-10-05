import sqlite3
from flask import g
from werkzeug.security import generate_password_hash

DATABASE = 'spendly.db'

def get_db():
    """
    Returns a SQLite connection with row_factory and foreign keys enabled.
    Uses Flask's 'g' object to ensure one connection per request.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON;")
    return g.db

def close_db(e=None):
    """Closes the database connection at the end of the request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    """Creates all tables using CREATE TABLE IF NOT EXISTS."""
    with sqlite3.connect(DATABASE) as conn:
        # Users table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Expenses table
        conn.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL,
                description TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        ''')
        conn.commit()

def seed_db():
    """Inserts sample data for development."""
    init_db()
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()

        # Check if users table already has data to prevent duplicates
        cursor.execute('SELECT count(*) FROM users')
        if cursor.fetchone()[0] > 0:
            return

        # Insert demo user
        demo_user = (
            'Demo User',
            'demo@spendly.com',
            generate_password_hash('demo123')
        )
        cursor.execute(
            'INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)',
            demo_user
        )

        user_id = cursor.lastrowid

        # Categories: Food, Transport, Bills, Health, Entertainment, Shopping, Other
        sample_expenses = [
            (user_id, 12.50, 'Food', '2026-10-01', 'Lunch at Cafe'),
            (user_id, 25.00, 'Transport', '2026-10-01', 'Fuel'),
            (user_id, 150.00, 'Bills', '2026-10-02', 'Electricity Bill'),
            (user_id, 45.00, 'Health', '2026-10-03', 'Pharmacy'),
            (user_id, 60.00, 'Entertainment', '2026-10-04', 'Movie Tickets'),
            (user_id, 80.00, 'Shopping', '2026-10-05', 'New T-shirt'),
            (user_id, 10.00, 'Other', '2026-10-05', 'Parking fee'),
            (user_id, 15.00, 'Food', '2026-10-06', 'Dinner'),
        ]

        cursor.executemany(
            'INSERT INTO expenses (user_id, amount, category, date, description) VALUES (?, ?, ?, ?, ?)',
            sample_expenses
        )
        conn.commit()
