# QBB2022 - Day 2 - Lunch Exercises Submission

#Exercise 1

#!/usr/bin/env python3

import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    #field_types = [str, int, int, str, float, str, int, int, 'place1', 'place2', 'place3', 'place4']
    field_types = [str, int, int, str, float, str, int, int, str, int, str, str]
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        if fieldN == 10 | fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        if fieldN == 9:
            fields[i] = fields[i].split(",")
            for l in fields:
                flength = len(fields[l])
                if flength != 3:
                    print(f"Line {i} appears malformed", file=sys.stderr)
                if flength == 3:
                    fields[l] = [ int(x) for x in fields[l] ]
        if fieldN == 12:
            for k in range(min(len(field_types), len(fields))):
                if k == 8:
                    fields[k] = fields[k].split(",")
                if k == 10:
                    fields[k] = fields[k].rstrip(",").split(",")
                if k == 11:
                    fields[k] = fields[k].rstrip(",").split(",")
            try:
                f9 = int(fields[9])
                f10 = int(len(fields[10]))
                f11 = int(len(fields[11]))
                assert f9 == f10
                assert f10 == f11
            except:
                print(f"Assert failed", file=sys.stderr)
                print(fields[9])
                print(len(fields[10]))
                print(len(fields[11]))
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
        bed.append(fields)
    fs.close()
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
