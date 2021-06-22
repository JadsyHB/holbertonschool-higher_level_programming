#!/usr/bin/env python3
"""
module 9
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    insert function
    """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
