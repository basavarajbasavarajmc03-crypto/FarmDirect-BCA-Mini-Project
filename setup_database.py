import os
import psycopg2

database_url = os.getenv("DATABASE_URL")

if not database_url:
    print("ERROR: DATABASE_URL is not set.")
    raise SystemExit(1)

try:
    with open("schema_postgres.sql", "r", encoding="utf-8") as f:
        sql = f.read()

    conn = psycopg2.connect(database_url)
    conn.autocommit = True

    with conn.cursor() as cur:
        cur.execute(sql)

    conn.close()
    print("SUCCESS: PostgreSQL database tables created.")

except Exception as e:
    print("ERROR:", e)