#Program to find the number of words in a file
#Developed by: Meyyappan.T
#Register no:212223240086
def program():
    count=0
    with open("text.txt","w") as f:
        f.write("This is a sample text to count the number of words")
    with open("text.txt","r") as f:
        for data in f:
            words=data.split()
            for word in words:
                count+=1
    print("Total number of words:",count)
program()