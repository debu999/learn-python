import psycopg2
from pp import pp
conn = psycopg2.connect(
    host = "dpg-clj0n24m411s73dusdv0-a.singapore-postgres.render.com",
    database = "pdb_yxsa",
    user="debabrata",
    password="Pgs4sIWKX152ntTr6Fb5ZCwiTGzAV1HB"
)

cur = conn.cursor()

create_investment_table = """
    create table investment (
        id serial primary key,
        coin varchar(32),
        currency varchar(3),
        amount real
    )
"""

cur.execute(create_investment_table)
conn.commit()
cur.close()
conn.close()

pp(["investment table created"])