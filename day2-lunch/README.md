# QBB2022 - Day 2 - Lunch Exercises Submission

#!/usr/bin/env python3
import sys

def parse_bed(fname):
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = []
    field_types = [str, int, int, str, float, str, int, int, 'place1', 'place2', 'place3', 'place4']
    for i, line in enumerate(fs):
        if line.startswith("#"):
            continue
        fields = line.rstrip().split()
        fieldN = len(fields)
        if fieldN < 3:
            print(f"Line {i} appears malformed", file=sys.stderr)
            continue
        if fieldN == 10 | fieldN == 11: #This line makes sure that bed files with 10 or 11 fields are not run.
            print(f"Line {i} appears malformed", file=sys.stderr)
        if fieldN == 9: #For bed 9 files
            fields[i] = fields[i].split(",") #remove comma delimited
            for l in fields: #for each field
                flength = len(fields[l]) #determine length of field
                if flength != 3: #if field does not equal 3
                    print(f"Line {i} appears malformed", file=sys.stderr) #Error
                if flength == 3: #if field equals 3
                    fields[l] = [ int(x) for x in fields[l] ] #Ensure integer
        if fieldN == 12: #if a bed12 file
            for k in range(min(len(field_types), len(fields))): #for each iteration
                if k == 8: #if its the 8th field
                    fields[k] = fields[k].split(",") #remove comma delimited
                if k == 10: #if its the 10th field
                    fields[k] = fields[k].rstrip(",").split(",") #remove comma delimited and the extra comma
                if k == 11: #if its the 11th field
                    fields[k] = fields[k].rstrip(",").split(",") #remove comma delimited and the extra comma
            try:
                f9 = int(fields[9]) #save value as int
                f10 = int(len(fields[10])) #save length as int
                f11 = int(len(fields[11])) #save length as int
                assert f9 == f10 #ensure these equal
                assert f10 == f11 #ensure these equal
            except:
                print(f"Assert failed", file=sys.stderr) #error
                print(fields[9]) #sanity value
                print(len(fields[10])) #sanity value
                print(len(fields[11])) #sanity value
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)
        fs.close()
        return bed

if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
