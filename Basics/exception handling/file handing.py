#reading file using python prg
##file=open("python.txt","r")
##stu=file.read(5)
##print(stu)
##file.close()
#get the charecter in read file
##file=open("python.txt","r")
##stu=file.read(10)
##print(stu)
##file.close()
#readline from the file
##file=open("python.txt","r")
##stu=file.readline()
##print(stu)
##stu1=file.readline()
##print(stu1)
##file.close()
#readlines from the file# output will come file is convert list
##file=open("python.txt","r")
##stu=file.readlines()
##print(stu)
##file.close()
#convert list text int original text
##import sys
##file=open("python.txt","r")
##stu=file.readlines()
##print("The contents in the files are:", stu)
##print("The contents in the filess are:")
##for line in stu:
##    sys.stdout.write(line)
##file.close()
##write file using python prg:
##c=""" Implement by van,
##first version 0.9.0"""
##filew=open("python.txt","w")
##filew.write("/n %s"%c)
##filew.close()
##writelines using python pg
##file=open("python.txt","w")
##list=[]
##for i in range(5):
##    color=input("enter the colour:")
##    list.append(color+"\n")
##file.writelines(list)
##file.close()
##copying a file
##file=open("python.txt","r")
##lines=file.read()
##file.close()
##
##filew=open("copypython.txt",'w')
##filew.write(lines)
##filew.close()
##
##print("The copy of the file is made")
##filew=open("copypython.txt",'r')
##lines=filew.read()
##print(lines)
##filew.close()
##delteing content from a file
##import sys
##f=open("python.txt","r")
##lines=f.readlines()
##print("Original content of the file:")
##for line in lines:
##    sys.stdout.write(line)
##f.close()
##del lines[1:4]
##
##f=open("python.txt","w")
##f.writelines(lines)
##f.close()
##print("\ndelting content : ")
##f=open("python.txt","r")
##lines=f.read()
##print(lines)
##f.close()
#update to the file
##import sys
##f=open("python.txt","r")
##lines=f.readlines()
##print("Original content of the file:")
##for line in lines:
##    sys.stdout.write(line)
##f.close()
##n=int(input("\n\nEnter the line number to change: "))
##if n <= len(lines):
##    r=input("Enter the new content: ")
##    lines[n-1]=r+"\n"
##    f=open("python.txt","w")
##    f.writelines(lines)
##    f.close()
##    print("The content of the file after updating line" ,n)
##    f=open("python.txt","r")
##    lines=f.read()
##    print(lines)
##    f.close()
##else:
##    print("The line number ",n , "is not found in the file")
##
##Accessing Specific Content in a File
##
##import linecache
##line=linecache.getline("python.txt",3)
##print("The content of the third line is: ", line)


str="Hello World"
f=open("filebinary.bin","wb")
f.write(str.encode('utf-8'))
f.close()
f=open("filebinary.bin","rb")
fcontent=f.read()
f.close()
print("The content in the file is :")
print(fcontent.decode('utf-8'))






