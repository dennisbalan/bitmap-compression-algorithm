#compress_index(bitmap_index, output_path, compression_method, word_size)
#Where: 'bitmap_index' is the input file that will be used in the compression. 'output_path'
#is the path to a directory where the compressed version will be written using the naming scheme
#specified above. 'compression_method' is a String specifying which bitmap compression method
#you will be using (WAH, BBC, PLWAH, etc). 'word_size' is an integer specifying the word size
#to be used.
import os.path
#compress_index takes the inputs specified in the comment block above and compresses the bitmap_index accoridng to compression method chosen
#and the word_size and writes the compressed bitmap to a new file in the chosen output_path
def compress_index(bitmap_index,output_path,compression_method,word_size):
    #The if statement checks to see if compression method is WAH and compresses the data according to that compression method
    if(compression_method == "WAH"):
        #open the bitmap_index as f for reading
        f = open(bitmap_index, "r")
        #create a new file that takes the name of the bitmap_index, adds the compression method and word_size to the file name and saves the file in the given input output_path
        file_name = bitmap_index + "_" + compression_method + "_" + str(word_size)
        output_file = os.path.join(output_path,file_name)
        #open the output_file you created for writing
        d = open(output_file,"w")
        #zero and one couunter count their named numbers
        zero_counter = 0
        one_counter = 0
        #run_counter count the number of runs
        one_run_counter = 0
        zero_run_counter = 0
        #word stores the bits that are in a compressed word
        word = []
        #stuff is all the lines in f that where read
        stuff = f.readlines()
        #for every line in stuff(the lines in f), compress the word. A compressed word may have bits from 2 lines
        for a in stuff:
            #collect the bits from a line in stuff(a) and add the bits to the word. For every one or zero increment the respective counter. Ignore newlines
            for b in a:
                if(b == '1'):
                    one_counter = one_counter + 1
                    word.append(b)
                if(b == '0'):
                    zero_counter = zero_counter+1
                    word.append(b)
                    #ignore newlines
                if(b == '\n'):
                    word = word
                #if number of bits is equal to word_size-1, you are good to start compressing.
                if(one_counter + zero_counter == word_size-1):
                    #for both the if and elif statements, check to see if the run counter is not 0. If it run counter is not 0, increment the run counter. If another run coutner is not 0, run the run_creator
                    #on the run to get the compressed run word, write it to the output file clear the word and reset the word array and previous run_counter
                    if(one_counter == 0):
                        if(one_run_counter != 0):
                            c = run_creator(1,zero_run_counter,word_size)
                            d.write(c)
                        word = []
                        one_counter = 0
                        zero_counter = 0
                        zero_run_counter = zero_run_counter + 1
                    elif(zero_counter == 0):
                        if(one_run_counter != 0):
                            c = run_creator(0,one_run_counter,word_size)
                            d.write(c)
                        word = []
                        one_counter = 0
                        zero_counter = 0
                        one_run_counter = one_run_counter +1
                    #if there is nor run, check to see if there is a run and if there is, run the run_creator on the run to get the compressed run word, write it to the output file 
                    #and clear the previous run_counter. Run the literal_creator on the word you have, write the result to the putput file and clear the word and all the counters
                    else:
                        if(one_run_counter != 0):
                            c = run_creator(1,one_run_counter,word_size)
                            one_run_counter = 0
                            d.write(c)
                        if(zero_run_counter != 0):
                            c = run_creator(0,zero_run_counter,word_size)
                            zero_run_counter = 0
                            d.write(c)
                        c = literal_creator(word)
                        d.write(c)
                        word = []
                        one_counter = 0
                        zero_counter = 0
        #close all the files
        f.close()
        d.close()
#literal_creator takes the input of a word array,adds a 0 to the front of the word array to signify a literal and turns the word array into a string and returns the same string
def literal_creator(word):
    a = "0"
    for b in word:
        a = a + b
    return a
#the run_creator takes the input of number, run_counter and word_size and create a run of run-counter size in word-size-2 bits, creatinh a run of "number" and returning it as a string
def run_creator(number,run_counter,word_size):
    #return string first bit is 1 to signify a run
    a = "1"
    #second bit signifies if run is a 0 or 1. This is determined by number, which can only be 0 or 1
    if(number == 0):
        a = a + "0"
    else:
        a = a + "1"
    #convert the run counter to binary
    b = bin(run_counter)
    #c is max number of runs in a word in binary
    c = 2 ^ (word_size-2)
    c = bin(c)
    #if the number of runs exceeds space in words, set number of runs b to c
    if(b > c):
        b = c
    #convert b to a string
    b = str(b)
    #find the number of bits that actually exist right now
    e = 2 + len(b) - 1
    #create a buffer of 0's between size f between a and b
    f = word_size - e
    g = ""
    for h in range(f):
        g = g + "0"
    #combine a,g,b to create a word and remove b for binary from the word. Return a as the compressed run
    a = a + g + b
    a = a.replace("b","")
    return a
#compress_index(R"C:\Users\Super D\Desktop\CS 351\HW4\Data\animals.txt","C:\Users\Super D\Desktop\CS 351\HW4\Data","WAH",64)
       

