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
            src.PrintColor.printAC()
            
            for URL in URLs:
                IDs.append(src.GetSubmitID.GetSubmitID(URL))
        else :
            print(usege)

    elif len(args) == 1:
        URLs = list(src.InputSTDIN.get_input())
        src.PrintColor.printAC()
        for URL in URLs:
            ID = src.GetSubmitID.GetSubmitID(URL)
            IDs.append(ID)

    else :
        print(usege)

    src.PrintIDs.PrintIDs(IDs,URLs)

