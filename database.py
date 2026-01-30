import sqlalchemy
import os
from google.cloud.sql.connector import Connector, IPTypes
from sqlalchemy import text

ip_type = IPTypes.PRIVATE if os.environ.get("PRIVATE_IP") else IPTypes.PUBLIC
connector = Connector(ip_type=ip_type, refresh_strategy="LAZY")

def getconn():
    conn= connector.connect(
        "project-586e4c98-e32a-46da-b1c:us-central1:github-repo-analyzer",
        "pymysql",
        user="root",
        password="gitrEpoadmin@2",
        db="github_repo_analyzer"
    )
    return conn

pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)
