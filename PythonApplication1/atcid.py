import src

if __name__ == '__main__':
    URL = str(input())
    ID = src.GetSubmitID.GetSubmitID(URL)
    print(ID)