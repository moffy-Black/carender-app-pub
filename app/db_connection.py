import psycopg2


def get_connection():
    DATABASE_URL = "postgres+psycopg2://db-url"
    return psycopg2.connect(DATABASE_URL)


if __name__ == "__main__":
    with get_connection() as conn:
        with conn.cursor() as cur:
            # cur.execute('SELECT * FROM users')
            # rows = cur.fetchall()
            # print(rows)
            cur.execute(
                "INSERT INTO users(name, time) values ('moffy', '2020-12-25 24:00:00')"
            )
            # cur.execute("DELETE FROM users")
        conn.commit()
