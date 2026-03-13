import sqlalchemy
import os
from google.cloud.sql.connector import Connector, IPTypes
from sqlalchemy import text
from dotenv import load_dotenv

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type=ip_type, refresh_strategy="LAZY")
load_dotenv()

DB_INSTANCE = os.getenv("DB_INSTANCE")
DB_DRIVER = os.getenv("DB_DRIVER")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

def getconn():
    conn= connector.connect(
        "project-586e4c98-e32a-46da-b1c:us-central1:github-repo-analyzer",
        "pymysql",
        user="root",
        password="gitrEpoadmin@2",
        db="github_repo_analyzer"
    )
    return conn

def connecttodatabase():
    pool = sqlalchemy.create_engine(
        "mysql+pymysql://",
        creator=getconn,
    )

    try:
        with pool.connect() as connection:
            connection.execute(text("SELECT 1"))
            print("Connection Established")
    except Exception as e:
        print(f"SQLAlchemy connection failed: {e}")
    finally:
        connection.close()