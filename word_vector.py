import numpy as np
import pandas as pd

def read_vectors(path):
    vectors = open(path,'r')
    days = vectors.read()

    def getVectorMap(vector):
        vector = vector.split()
        return {str(vector[0]), tuple(vector[1:])}

    vectorMap = {}
    vectors = []
    for vector in days.split('\n'):
        vector = vector.split()
        if len(vector) > 300:
            vectorMap[vector[0]] = tuple(vector[1:])
            # vectors.append(vector[0])
    # return vectors
    return vectorMap
    # vectorMap = [getVectorMap(vector) for vector in days.split('\n')]

words = read_vectors('./sources/wiki.zh.vec')
pass
