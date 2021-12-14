#!/usr/bin/env python3
"""
This module contains a function that list all document in a collection
"""


def list_all(mongo_collection):
    """
    this method lists all documents in a collection

    Args: mongo_collection as the pymongo collection object
    Returns:
         list of documents or empty list if no document is in the collection
    """
    return mongo_collection.find()
