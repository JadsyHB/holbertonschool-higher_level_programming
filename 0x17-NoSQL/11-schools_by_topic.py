#!/usr/bin/env python3
"""
module 11
"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    return list
    """
    return [i for i in mongo_collection.find({"topics":topic})]
