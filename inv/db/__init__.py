import motor.motor_asyncio
import os


def get_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db = client.db_f608
    return db
