#!/usr/bin/env python3
"""
This module contains a function that insert a new document in a collection
base on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    this function adds a new document to an existing collection
    Args:
        pymongo collection object: mongo_collection
        kwargs: dictionary of a new document to insert

    Returns:
        id of the added new document
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
