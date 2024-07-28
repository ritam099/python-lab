def onlyLastLetters(tuple):
    result = []
    for i in tuple:
        result.append(i[-1])
    return result
    
tuplePrint= ("python", "learn", "includehelp")
answer = onlyLastLetters(tuplePrint)
print(answer)