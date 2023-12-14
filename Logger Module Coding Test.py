
import datetime
import time
import unittest

class LogComponent:
    def __init__(self, log_directory):
        self.log_directory = log_directory

    def write(self, text):
        cur_time = datetime.datetime.now() #capturing the current time

        #file_path = ".../../../file.txt" #stating the file path
        f = open("file.txt", "x") #open file
        f.write("...") #writing on the file 
    
    #def stop(self, text): 
        #case 1 - stopping right away - any outstanding writing is NOT done
        #case 2 - wait, until finishing outstanding writing

#class Unittest:
    #def write:
        #self.log_directory = "logs"
        #...
        #Initiate, conduct the LogComponent, until the writing

    #def newfile:
        #capture the updated/new current time 
        #bring LogComponent.cur_time 
        #Make a condition - if the updated time contains 'Hour' of '00' using the datetime format - midnight is crossed
            #if True, f. = open("file.txt", "s") #Make a new file
        #Continue the step of writing - LogComponent.write

    #def stoptime:
        #Stop LogComponent
            #case 1 - if outstanding logs are NOT written
            #wait for LogComponent to be conducted