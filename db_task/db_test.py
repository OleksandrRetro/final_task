import os
import random
import string

import sqlalchemy as db
from sqlalchemy import text

TABLE_NAME = "users"

postgres_url = os.getenv("POSTGRES_URL")
engine = db.create_engine(postgres_url, echo=True)
metadata_obj = db.MetaData()

user = db.Table(
    TABLE_NAME,
    metadata_obj,
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('name', db.String),
    db.Column('age', db.Integer),
)


def test_create_table():
    if not engine.dialect.has_table(engine, TABLE_NAME):
        metadata_obj.create_all(engine, [user])
    assert engine.dialect.has_table(engine, TABLE_NAME)


def test_insert_and_select():
    name = ''.join(random.choice(string.ascii_lowercase) for _ in range(10))
    engine.execute(
        user.insert().values(
            name=name,
            age=18
        )
    )

    query = text(f"SELECT name FROM {TABLE_NAME} WHERE name='{name}'")

    result = engine.execute(query).fetchone()
    assert result[0] == name
