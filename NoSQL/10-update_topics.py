#!/usr/bin/env python3
"""
Module that updates all topics of a school document based on the name.
"""

def update_topics(mongo_collection, name, topics):
    """
    Updates all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): the school name to update.
        topics (list): list of strings representing the topics.

    Returns:
        None.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    