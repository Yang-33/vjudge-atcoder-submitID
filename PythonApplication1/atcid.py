import src
import sys



if __name__ == '__main__':
    IDs = []
    URLs = []
    usege = 'Usage: python {} [-f FILE] [--help]'\
            .format(__file__)
    args = sys.argv

    if len(args) == 3: # file mode
        if args[1] == "-f":
            URLs = src.GetFromfileURL.GetfromfileURL(args[2])
            for URL in URLs:
                IDs.append(src.GetSubmitID.GetSubmitID(URL))
        else :
            print(usege)
    elif len(args) == 1:
        URL = str(input())
        ID = src.GetSubmitID.GetSubmitID(URL)
        IDs.append(ID)
        URLs.append(URL)
    else :
        print(usege)

    src.PrintIDs.PrintIDs(IDs,URLs)
