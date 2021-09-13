import os
from pymongo import MongoClient

mongo = MongoClient(os.environ['MONGO_URI'], ssl=True,ssl_cert_reqs='CERT_NONE')