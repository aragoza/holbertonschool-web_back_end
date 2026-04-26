#!/usr/bin/env python3

"""
List all the documents in collection of a db
"""


def list_all(mongo_collection):
    """
    List all document in mongo_collection
    """

    if mongo_collection.find():
        return mongo_collection.find()

    return []
