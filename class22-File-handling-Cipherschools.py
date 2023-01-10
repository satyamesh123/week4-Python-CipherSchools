Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> file=open("random.txt","w")
... file.write("blah blah blah")
... file.close()
... file=open("random.txt","w")
... file.write("Jatin Katyal")
... file.write("\n new line")
... a=["jatin","sanarth","sujith","saranah"]
... file.writelines(a)
... for i in a:
...     file.write(i)
... file.close()
... 
... # Reading from a file
... file=open("sample.txt","r")
... print(file.read())
... 
... # Smarter way of opening files...
... with open("random.txt","r") as file:
