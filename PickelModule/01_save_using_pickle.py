import pickle

list1 = [1,2,3,4,5,6]# object to be saved
fileName= "data.pickle" # fileName
# saving Object using pickle module
with open(fileName,"wb") as fileHandle:
    pickle.dump(list1, fileHandle)# dump method of pickle module is used to save object in to file






# fileHandle = open(fileName, "wb")
# pickle.dump(list1, fileHandle)
# fileHandle.close()
# try: 
#     with open(fileName,"wb") as fileHandle:
#         pickle.dump(list1, fileHandle)
#     print("Object Save Successfully")
# except:
#     print("Error Occured Saving Object")



    