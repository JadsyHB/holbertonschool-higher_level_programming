#!/usr/bin/env python3
"""
list all docs in collection
"""

import pymongo


def list_all(mongo_collection):
    """
    list all function
    """
    if mongo_collection:
        return list(mongo_collection.find())
    return []
