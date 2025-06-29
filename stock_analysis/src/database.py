"""Database module.

Provides functions to interact with the SQLite database.
"""

import sqlite3


def init_db(path: str):
    """Initialize the database at the given path."""
    conn = sqlite3.connect(path)
    conn.close()
