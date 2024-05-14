#!/usr/bin/env python3
""" Write function that returns all students sorted by average """


def top_students(mongo_collection):
    """ Write function returns all students sorted by average """
    return mongo_collection.aggregate([
        {"$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
