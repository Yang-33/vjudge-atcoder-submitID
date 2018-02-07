
def GetfromfileURL(filename):
    URL = []
    with open(filename,'r') as File:
        for line in File:
            URL.append(line)
    return URL
