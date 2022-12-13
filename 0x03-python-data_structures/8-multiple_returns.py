#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if sentence:
        return(size, sentence[0])
    else:
        return(0, None)
