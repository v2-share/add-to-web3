import certifi
import pymongo
import sys
import argparse
from bson.json_util import dumps

parser = argparse.ArgumentParser(description='Insert data to mongdb.net')
parser.add_argument("--con", help="Connection url", default="")
parser.add_argument("--name", help="Insert name", default="")
parser.add_argument("--cid", help="Insert cid", default="")
parser.add_argument("--size", help="Insert size", default="")

args = parser.parse_args()


if args.cid is None:
  print("Nothing to save")
  quit()


client = pymongo.MongoClient(args.con, tlsCAFile=certifi.where())
mydb = client["mydb"]
mycol = mydb["web3"]
taskcol = mydb["task"]


mydict = {"name":args.name,"cid": args.cid,"size": args.size,"issync":0}
x = mycol.insert_one(mydict)

keyword="##"+args.name
task = taskcol.find_one({'url':{'$regex':keyword}})
taskcol.delete_one(task)

print(x)
