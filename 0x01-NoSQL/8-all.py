#!/usr/bin/env python3
""" function that lists all documents in a collection """


def list_all(mongo_collection) -> list:
    """ function that lists all documents in a collection """
    return mongo_collection.find()
