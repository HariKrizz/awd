
#1
#write
newFile = open("demo.txt","w")
newFile.write("Hello there, I'm a challenge") 
newFile.close()

#2
#read
newFile = open("demo.txt","r")
new = newFile.read()
print(new)

#3
#append         
newFile = open("demo.txt","a")
new_append = newFile.write("\nLine added to the file")
newFile.close()

