#create_index(input_file, output_path, sorted)
#Where: 'input_file' is a file that you will use to create the bitmap index. 'output_path' is the
#destination directory for your output bitmap file. It must be a regular file with no suffixes
#(.txt, .c, etc). 'sorted' is a boolean value that specifies whether your data will be sorted.
import os
import os.path
from operator import itemgetter
#as the description above says,create_index creates a bitmap_index based on the inpu_file, saves it as a new file in output_path, and ma sort it if srited is True
def create_index(input_file,output_path,sorted):
    #if sorted is true, sort the input_file
    if(sorted == True):
        sort_stuff(input_file)
    #open the input file for reading
    f = open(input_file,"r")
    #create new file for output in the output_path and open it for writing
    file_name = input_file
    if(sorted == True):
        file_name = file_name + "_sorted"  
    output_file = os.path.join(output_path,file_name)
    a = open(output_file,"w")
    #save all the element of input_file in stuff
    stuff = f.readlines()
    #b is the string to which the bitmap will written to
    b = ""
    #split the tuples(word) in each line and evaluate each element and convert it to a bitmap, the animal, age and adopeted boolean should be added to the bitmap
    for line in stuff:
        words = line.split(',')
        b = animal_bits(words)
        b = b + age_bits(words)
        b = b + bool_check(words)
        #add the newline to string after being done
        b = b + "\n"
        #write b to the output_file a
        a.write(b)
    #close the files
    a.close()
    f.close()
#animal bits takes the input of words(a tuple) and determines what the first 4 bits of the bitmap will be written to a string. the string will be returned
def animal_bits(words):
    j = ""
    if(words[0] == "cat"):
        j = "1000"
    if(words[0] == "dog"):
        j = "0100"
    if(words[0] == "turtle"):
        j = "0010"
    if(words[0] == "bird"):
        j = "0001"
    return j
#age bits returns a string of 10 chars where there is one 1 in a location corresponding to the age of the animal 
#age_bits takes an input of the tuple words and will work on its second element
def age_bits(words):
    #convert second element of words from string to int in c. That is the age of the animals
    c = int(words[1])
    d = 0
    #determine the range of c. This will be the location of the 1 bit int the word. It will be saved in d
    if(c <= 10):
        d = 0
    if(c > 10 and c <= 20):
        d = 1
    if(c  > 20 and c <= 30):
        d = 2
    if(c > 30 and c <= 40):
        d = 3
    if(c > 40 and c <= 50):
        d = 4
    if(c > 50 and c <= 60):
        d = 5
    if(c > 60 and c <= 70):
        d = 6
    if(c > 70 and d <= 80):
        d = 7
    if(c > 80 and c <= 90):
        d = 8
    if(c > 90 and c <= 100):
        d = 9
    string = ""
    #create the string of 10 bits, with 0's in most of the string and 1 in the d location of the string
    for x in range(10):
        if(x == d):
            string = string + "1"
        else:
            string = string + "0"
    #return the string
    return string
#bool_check takes the input of the tuple array and returns a string of 2 bits that differs when string contains True or False
def bool_check(array):
    array[2].strip('\n')
    #save the 2nd element of the tuple in c, it contains the boolean
    c = array[2]
    string = ""
    #determine the bits to write to the string based on the boolean
    if(c.find("True") != -1):
        string = string + "10"
    if(c.find("False") != -1):
        string = string + "01"
    #return the string
    return string
#sort_stuff sorts the input file. It will actually physically change the file
def sort_stuff(input):
    #open the input file for reading
    f = open(input,"r")
    #save all the lines in the file in array
    array = f.readlines()
    #sort the lines
    array = sorted(array,key = itemgetter(0))
    #close the file
    f.close()
    #now open for writing
    a = open(input,"w")
    string = ""
    #write all the lines back into file
    for b in array:
        string = string + b
        if b.find("True") != -1 or b.find("False") != -1:
            a.write(string)
            string = ""
    #close the file
    a.close()
#create_index("animals.txt","C:\Users\Super D\Desktop\CS 351\HW4\Data",False)
