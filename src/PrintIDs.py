from . import PrintColor

def PrintIDs(IDs,Names=None):
    if Names == None:
        PrintColor.ColumnID("ID")
        for id in IDs:
            print("",id)
    else :
        PrintColor.ColumnID("ID URL")
        for id,Name in zip(IDs,Names):
            print("",id," ", Name)

#ids = [123,121,121212]
#names = [1,1,1]

#PrintIDs(ids,names)
#PrintIDs(ids)