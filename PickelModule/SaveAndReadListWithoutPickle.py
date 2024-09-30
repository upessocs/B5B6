# Save a list in to a file
filePath = 'listData.txt'
data = [1,2,3,4]

with open(filePath, "w") as fileHandle:
    fileHandle.write(str(data)) 

# Read the same file and recover data as list
with open(filePath,"r") as fileHandle:
    readData = fileHandle.read()
    print(f"data read is {readData} \nits type is {type(readData)} and \nlength is {len(readData)}")
    tempvar=readData[1:len(readData)-1].replace(" ",'')
    print(tempvar)
    listPlaceholder=tempvar.split(",")
    recoveredList = listPlaceholder
    print(f"recovered List is {recoveredList}\n its type is {type(recoveredList)}")
    
    