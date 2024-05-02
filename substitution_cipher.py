import string 

dict = {}
data = ""
file=open("output_file.txt","w")
for i in range(len(string.ascii_letters)) :
    dict[string.ascii_letters[i]] = string.ascii_letters[i-1] 
print(dict)
with open("input_file.txt") as f:
    while True:
        content=f.read(1)
        if not content:
            print("End of file.")
            break
        if content in dict :
            data= dict[content]
        else:
            data=content
        file.write(data)
        print(data)
file.close()