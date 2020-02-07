from nferx_py import fn as nf
from pymongo import MongoClient

nf.authenticate('nfer','6eaa1d27bfa0639f2712191fa55df872')
nf.modify_defaults('server', 'pre-staging')
nf.modify_defaults('api_server', 'pre-staging')
AUTH = nf.AUTH

client = MongoClient('mongodb://deeksha:pg599ohismw1bio@mongo.servers.nferx.com:27017/')
mongo_db_name='ci_intermediate_db'
mongo_db_collection='ctrials_data_0203'
db = client[mongo_db_name]
coll = db[mongo_db_collection]