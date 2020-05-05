#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or not sentence:
        return(0, None)
    return(len(sentence), sentence[0])
