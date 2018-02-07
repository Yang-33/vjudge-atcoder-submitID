import src
import sys


def GetfromfileURL(filename):
    URL = []
    with open(filename,'r') as File:
        for line in File:
            URL.append(line)
    return URL

if __name__ == '__main__':
    IDs = []
    URLs = []
    usege = 'Usage: python {} [-f FILE] [--help]'\
            .format(__file__)
    args = sys.argv
    if len(args) == 3: # file mode
        URLs = GetfromfileURL(args[2])
        for URL in URLs:
            IDs.append(src.GetSubmitID.GetSubmitID(URL))
    elif len(args) == 1:
        URL = str(input())
        ID = src.GetSubmitID.GetSubmitID(URL)
        IDs.append(ID)
        URLs.append(URL)
    else :
        print(usege)

    src.PrintIDs.PrintIDs(IDs,URLs)
