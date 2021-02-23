import sheet

read = sheet.read("Sheet1!A1:D10")
consumer = input("Enter the name of the person's whose food order you want to check ")
for i in read:
    for j in i:
        if j == consumer:
            print("The consumer's food is", i[1])
