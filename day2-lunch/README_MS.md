# QBB2022 - Day 2 - Lunch Exercises Submission

#Exercise 1

#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r') #open file
    except:
        raise FileNotFoundError("That file doesn’t appear to exist") #Error
    bed = [] #Initialize list
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str] #string of field types for conversion
    for i, line in enumerate(fs): #for each line in file
        if line.startswith("#"): #remove header lines
            continue
        fields = line.rstrip().split() #columns?
        fieldN = len(fields) #count of columns
        if fieldN < 3: #if field is less than three
            print(f"Line {i} appears malformed", file=sys.stderr) #error
            continue
        if fieldN == 10 | fieldN == 11: #if its 10 or 11
            print(f"Line {i} appears malformed", file=sys.stderr) #error
            continue

######################################################################
Everything about here looks correct. You've checked that the number of
fields is appropriate and gotten rid of the header line.
######################################################################


        if fieldN == 9: #if its bed9
            fields[i] = fields[i].split(",") #remove commas
            for l in fields: #for column
                flength = len(fields[l]) count length
                if flength != 3: #not equal to 3
                    print(f"Line {i} appears malformed", file=sys.stderr) #error
                if flength == 3: #equal to 3
                    fields[l] = [ int(x) for x in fields[l] ] #ensure it is an int

######################################################################
This block of code has some errors. After you check if there are 9
fields, you reference fields[i]. Remember that i is holding the line
number of the file you're reading in, while fields is a list of the
columns in each entry. You want to refer to the itemRGB column in this
line (index 8) when you split the field by commas. Then you want to 
check that there are only 3 values in the field. Since it is only one
field, you don't need to do a for loop. Instead, you can just check
that one entry

if len(fields[8]) != 3:

Then you can use a for loop to convert each entry into an integer. You need to use range so that you can refer to a specific item in fields[8]
and change it in place.

for j in range(3):
    fields[8][j] = int(fields[8][j])

Finally, if you bed file has more than 9 columns, you still need to do
this check, so you should be checking if fieldN >= 9
######################################################################

        if fieldN == 12: #for bed 12
            for k in range(min(len(field_types), len(fields))): #for each iteration
                if k == 8: #for column 9
                    fields[k] = fields[k].split(",") #remove commas
                if k == 10: #for c11
                    fields[k] = fields[k].rstrip(",").split(",") #remove commas and final comma
                if k == 11: #for c12
                    fields[k] = fields[k].rstrip(",").split(",") #remove commas and final comma

######################################################################
Here, you are repeating your efforts on the itemRGB column. It works,
but you could save yourself the work by making the previous code chunk
execute if fieldN >= 9. Also, this solution works for splitting up
fields 9, 11, and 12. However, since it is only 3 fields you could
just skip the for loop and replace k with 8, 10, and 11, respectively
for each line following your if satements

fields[8] = fields[8].split(",")
fields[10] = fields[10].rstrip(",").split(",")
fields[11] = fields[11].rstrip(",").split(",")
######################################################################

            try:
                f9 = int(fields[9]) #count
                f10 = int(len(fields[10])) #Count length
                f11 = int(len(fields[11])) #count length
                assert f9 == f10 #make sure theyre equal
                assert f10 == f11 #make sure theyre equal
            except:
                print(f"Assert failed", file=sys.stderr) #error
                print(fields[9]) #print the numb
                print(len(fields[10])) #print the numb
                print(len(fields[11])) #print the numb

######################################################################
This is a nice use of assert. It works will wrapped in the try
statement
######################################################################

        try:
            for j in range(min(len(field_types), len(fields))): #for each iteration
                fields[j] = field_types[j](fields[j]) #convert the fields to the right type

######################################################################
This block needs to come before you do any data conversions to fields
9, 11, or 12. If it comes after, it will take the converted field
and change it back into a string.
######################################################################

        except:
            print(f"Line {i} appears malformed", file=sys.stderr) #error
        bed.append(fields) #add to the bed field
    fs.close() #close the file
    return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
    print(bed)
	
	
	
#Exercise 2

import sys
import statistics

import bed_parser
fname = sys.argv[1]
bed = bed_parser.parse_bed(fname)
medvals = []
lengthbed = len(bed)
for i in range(0,lengthbed):
    medvals.append(int(bed[i][9]))

print(statistics.median(medvals))

 #There are 3 malformed lines
 #The median is 4

######################################################################
Nice use of the median function. Overall, there were a couple of
issues, but you appear to be in pretty good shape understanding and
writing the logic needed to address the problem into your programs.
Just be careful when indexing lists to make sure you know what field
you are trying to get and what you are using as an index. Overall,
you are doing really well. Keep it up! - Mike
######################################################################

