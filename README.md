# Word-count
## AIM:
To write a python program for getting the word count from a text.
## EQUIPEMENT'S REQUIRED: 
PC
Anaconda - Python 3.7
## ALGORITHM: 
### Step 1:
Create a file with .txt file extension.

### Step 2: 
Add some texts in that file.

### Step 3: 
Create a python file.

### Step 4:  
Write a code to count the number of words in that file.

### Step 5: 
Run the program.

### Step 6: 
Display the output.

## PROGRAM:
```
#Developed by: Meyyappan.T
#Register Number: 212223240086
def program():
    count=0
    with open("text.txt","r") as f:
        for data in f:
            words=data.split()
            for word in words:
                count+=1
    print("Total number of words:",count)
program()
```

### OUTPUT:
![image](https://github.com/marcoyoi/Word-count/assets/128804366/79d06a34-1652-439b-aca7-e6b87f703910)
![image](https://github.com/marcoyoi/Word-count/assets/128804366/f6a8fe8c-eea3-4eaf-8231-88d6f43c0487)
![image](https://github.com/marcoyoi/Word-count/assets/128804366/0ea1393d-5eb2-4b8a-aa98-30b8c2c4b06e)

## RESULT:
Thus the program is written to find the word count from a text.
