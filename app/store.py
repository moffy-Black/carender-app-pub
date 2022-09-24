from app.db_connection import get_connection
from psycopg2.extras import DictCursor

def insert_data(name,time):
  # --- データの挿入 ---
  with get_connection() as conn:
    with conn.cursor() as cur:
      cur.execute(f"INSERT INTO users(name, time) VALUES('{name}', '{time}')")

def remove_data(name,time):
  # --- データを取り除く ---
  with get_connection() as conn:
    with conn.cursor() as cur:
      cur.execute(f"DELETE FROM users WHERE name='{name}' AND time='{time}'")

def select_data():
  #データの取り出し
  with get_connection() as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
      cur.execute(f"SELECT * FROM users")
      rows = cur.fetchall()

  return rows

def select_filter_data(name):
  #カラム(name)内のデータだけ取り出す
  with get_connection() as conn:
    with conn.cursor(cursor_factory=DictCursor) as cur:
      cur.execute(f"SELECT * FROM users WHERE name = '{name}'")
      user_rows = cur.fetchall()
  return user_rows