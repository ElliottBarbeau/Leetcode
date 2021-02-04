def reorderLogFiles(logs):
    front = []
    back = []
    for log in logs:
        #If it is a letter log, append to the front list, otherwise append to the back.
        if log.split()[1].isdigit():
            back.append(log)
        else:
            front.append(log)
    
    #Sort letter-logs lexicographically and by identifier
    front.sort(key = lambda x: x.split()[0])
    front.sort(key = lambda x: x.split()[1:])
    ret = front + back
    return ret
print(reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))