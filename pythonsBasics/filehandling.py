
#open the file
# file=open("D:\\Study\\Python\\py+sel\\pythonsBasics\\my_file.txt","r")
# file=open("D:/Study/Python/py+sel/pythonsBasics/my_file.txt","r")

#read the file content
# file=open('my_file.txt','r')
# content=file.read()
# print(content)
# file.close()

#readline
# file=open('my_file.txt','r')
# line=file.readline()
# print(line)
# file.close()

# file=open('my_file.txt','r')
# line=file.readline()
# while line:
#     print(line.strip())
#     line=file.readline()
# file.close()

#readlines
# file=open('my_file.txt','r')
# lines=file.readlines()
# print(lines)
# file.close()

#writing in a file.
# file=open("my_file1.txt","w")
# file.write("Hello World this is my new line insert\n")
# file.write("Writing files using python\n")
# file.close()

# #appending in files.
# file=open("my_file1.txt","a")
# file.write("this is my line that is being appended")
# file.close()

#Cleaner approach to read a file.
# with open ("my_file1.txt", "r") as file:
#     content=file.read()
#     print(content)

#opening an image file.
# file=open("test.jpg","br")
# content=file.read()
# print(content)
# file.close()

#opening a non-existing file
# file=open("file.txt","r")
# file.close()
# try:
#     file=open('test.txt')
# except FileNotFoundError:
#     print('File was not found')

#reading a config or an .ini file.

# import configparser
# config=configparser.ConfigParser()
#
# config.read('config.ini')
#
# host=config['database']['host']
# port=config.getint('database','port')
# editable=config.getboolean("app","readonly")
#
# print(f"the host is {host}")
# print(f"the port is {port}")
# print(f"the editable value is {editable}")
#


