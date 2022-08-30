#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import module
filename = sys.argv[1] #set input filename
if len(sys.argv) >2: #if user provides desired lines
    n_lines = int(sys.argv[2]) #set the desired number of lines
else: #otherwise
    n_lines = 10 #set the desired number of lines to default
Lstorage = []
for i, line in enumerate(open(filename)):
    Lstorage.append(line)
lastlines = Lstorage[-n_lines:]
for line in lastlines: #FOR every line in the open file
    print(line.strip('\r\n')) #print the line

#First, we need to SET the input file
#Next, IF the user-specified a desired number of lines to display
    #THEN we need to SET the desired number of displayed lines
#END IF
#otherwise
    #Then we need to set the desired number of displayed lines to a default
#End otherwise
#SET a storage list for lines in the file
#Then, for every line in the open file
    #add the line to the storage list
#End For
#SET a subset of the storage list to be the last desired number of items in the storage list
#for every line in the subset
    #print every line in the subset
#END For

# This script is spot on. It's got good comments, clear logic and it does exactly
# what it's supposed to. The only feedback I've got is that if you include 
# blank lines to break up your code into functional blocks, it would make it
# more readable and understandable. Other than that, it looks great. Keep it up!
# - Mike