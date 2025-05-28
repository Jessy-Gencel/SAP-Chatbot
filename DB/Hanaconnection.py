import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import reflection, Connection
from sqlalchemy.engine.reflection import Inspector
from hdbcli import dbapi

# Load variables from .env
load_dotenv()

# Get HANA credentials from environment variables
HANA_HOST = os.getenv("HANA_ADRESS")
HANA_PORT = os.getenv("HANA_PORT")
HANA_USER = os.getenv("HANA_USER")
HANA_PASSWORD = os.getenv("HANA_PASSWORD")

def get_sqlalchemy_engine() -> tuple[Connection, Inspector]:
    """Create and return an SQLAlchemy engine connection and inspector for SAP HANA"""
    try:
        engine = create_engine(
            f'hana://{HANA_USER}:{HANA_PASSWORD}@{HANA_HOST}:{HANA_PORT}',
            connect_args={
                'encrypt': 'true',
                'sslValidateCertificate': 'false',
            },
            echo=True
        )
        connection: Connection = engine.connect()
        inspector: Inspector = reflection.Inspector.from_engine(engine)
    except Exception as e:
        print(f"Error creating SQLAlchemy engine: {e}")
        raise
    return connection, inspector

connection, inspector = get_sqlalchemy_engine()
