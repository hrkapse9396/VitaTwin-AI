from sqlalchemy import create_engine, inspect


DATABASE_URL = "sqlite:///database/vitatwin.db"


engine = create_engine(DATABASE_URL)


inspector = inspect(engine)


tables = inspector.get_table_names()


print("Database Tables:")
for table in tables:
    print(table)