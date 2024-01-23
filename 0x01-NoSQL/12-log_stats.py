#!/usr/bin/env python3
"""Log stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    logs_collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{logs_collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        count = logs_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    cnt = logs_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{cnt} status check")
