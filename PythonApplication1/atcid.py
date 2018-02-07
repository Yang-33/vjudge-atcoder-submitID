import src
import sys
from colorama import init

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
        URLs = list(src.InputSTDIN.get_input())
        for URL in URLs:
            print("URL is,",URL)
            ID = src.GetSubmitID.GetSubmitID(URL)
            IDs.append(ID)

    else :
        print(usege)

    src.PrintIDs.PrintIDs(IDs,URLs)

    #OKBLUE = '\033[94m'
    #OKGREEN = '\033[92m'
    #WARNING = '\033[93m'
    #FAIL = '\033[91m'
    #ENDC = '\033[0m'

    #print (OKBLUE + 'Blue' + ENDC)
    #print (OKGREEN + 'Green' + ENDC)
    #print (WARNING + 'Warning' + ENDC)
    #print (FAIL + 'Fail' + ENDC)