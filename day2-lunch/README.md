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
        if fieldN == 9: #if its bed9
            fields[i] = fields[i].split(",") #remove commas
            for l in fields: #for column
                flength = len(fields[l]) count length
                if flength != 3: #not equal to 3
                    print(f"Line {i} appears malformed", file=sys.stderr) #error
                if flength == 3: #equal to 3
                    fields[l] = [ int(x) for x in fields[l] ] #ensure it is an int
        if fieldN == 12: #for bed 12
            for k in range(min(len(field_types), len(fields))): #for each iteration
                if k == 8: #for column 9
                    fields[k] = fields[k].split(",") #remove commas
                if k == 10: #for c11
                    fields[k] = fields[k].rstrip(",").split(",") #remove commas and final comma
                if k == 11: #for c12
                    fields[k] = fields[k].rstrip(",").split(",") #remove commas and final comma
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
        try:
            for j in range(min(len(field_types), len(fields))): #for each iteration
                fields[j] = field_types[j](fields[j]) #convert the fields to the right type
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
