#!/usr/bin/env python3
"""Improved log stats module"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017/')
    collection = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")

    cnt = logs_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{cnt} status check")

    print("IPs:")
    ips = db.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for ip in ips:
        print(f"\t{ip.get('ip')}: {ip.get('count')}")
