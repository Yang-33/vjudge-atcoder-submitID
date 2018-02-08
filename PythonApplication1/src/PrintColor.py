
from colorama import init

def printAC():
    CYAN = '\033[96m'
    ENDC = '\033[0m'

    ACMes = "Acceptance"
    print(" [" + CYAN + ACMes + ENDC + "]")

def test():
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    BLUE = '\033[34m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    ACMes = "Acceptance"
    #print ("["+ OKBLUE + ACMes + ENDC + "]")
    print("[" + BLUE + ACMes + ENDC + "]")
    #print (OKGREEN + 'Green' + ENDC)
    #print (WARNING + 'Warning' + ENDC)
    #print (FAIL + 'Fail' + ENDC)
def ne():
    TEMPLATE = '\033['
    BLUE = '\033[96m'
    ENDC = '\033[0m'

    ACMes = "Acceptance"
    
    for num in range(1,108):
        COLOR = TEMPLATE + str(num) + "m"
        print(num,"[" + COLOR + "TEXT" + ENDC + "]")
    print("[" + BLUE + ACMes + ENDC + "]")

def ColumnID(Mode):
    Mes = ""
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    ENDC = '\033[0m'

    if Mode.find("ID") != -1 :
        Mes = " ["+ GREEN+ "ID"+ ENDC + "]"
        if Mode.find("URL") :
            Mes = Mes + "   ["+ YELLOW + "URL"+ ENDC + "]" 
    
    print(Mes)
#printAC()
#ne()