#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
x= input('enter the string---->')
Lower=0
Upper=0
for i in x:
    if i.islower():
       Lower=Lower+1
    elif i.isupper():
        Upper=Upper+1
print('No. of Upper characters :', Upper)  
print('No. of Lower characters :', Lower)           
