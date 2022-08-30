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
        if fieldN == 10 | fieldN == 11:
            print(f"Line {i} appears malformed", file=sys.stderr)
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
                if k == 10 | k == 11:
                    fields[k] = fields[k].rstrip(',').split(',')
            try:
                assert fields[9] == len(fields[10])
                assert fields[9] == len(fields[11])
            except:
                print(f"Assert failed", file=sys.stderr)
                print(fields[9])
                print(len(fields[10]))
                print(len(fields[11]))
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
