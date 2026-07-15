file = r'C:\Users\Deepa Moirangthem\OneDrive\Desktop\python\learning_python\deepa\contact book\otherFile.txt'
#     print(f.read()) ----> (this is for other folder file read)

try:
    with open(file,"x") as f:
        f.write("hello world")
        print("added text")
        print(f"the text contents is: {f.read()}")
except FileNotFoundError:
    print("file already exists.")

    with open(file,"a") as f:
        f.write("\nAdded a new line")




    with open(file,"r") as f:
        print(f"the text contents is: {f.read()}")

    #     f.write(" added text")
    

# with open("file.txt") as f: ----> (this is for read in a same folder)
#     print(f.read())


