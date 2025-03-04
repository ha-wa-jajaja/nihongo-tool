from app.db.database import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SHOW TABLES"))
            print("Database connection successful!")
            return True
    except Exception as e:
        print(f"Database connection failed: {e}")
        return False

if __name__ == "__main__":
    test_connection()