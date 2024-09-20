# program to read csv file and return a list of list

fileName = "data.csv"

# function to read csv file and return list
def read_csv(file_name):
    ext = file_name.split(".")[-1].lower()
    assert ext == "csv", "Invalid file type"

    fileHandle = open(file_name,"r")
    data = fileHandle.read()
    fileHandle.close()

    # your logic
    rows = data.split("\n")
    # print("\n")
    # print(rows)

    for i in range(0,len(rows)):
        row = rows[i]
        rows[i] = row.split(",")
    # print("\n")
    # print(rows)
    op = rows
    return op# it should return list of list

receivedData = read_csv(fileName)


print(receivedData[9][2])
