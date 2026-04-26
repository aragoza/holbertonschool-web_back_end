#!/usr/bin/env python3

"""
list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    list of school having a specific topic
    """
    list_data = []

    for dictio in mongo_collection.find():
        if "topics" in dictio and topic in dictio["topics"]:
            list_data.append(dictio)

    return list_data
