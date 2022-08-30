 # QBB2022 - Day 2 - Homework Excercises Submission
 
 #!/usr/bin/env python

 import sys #importing sys for usability

 def parse_vcf(fname): #making the parse_vcf function
     vcf = [] #make a list for vcf
     info_description = {} #make a dictionary for info_description
     info_type = {} #make a dictionary for info type
     format_description = {} #make a dictionary for format_description
     type_map = { #making a dictionary and naming each type
         "Float": float,
         "Integer": int,
         "String": str
         }
     malformed = 0 #setting a counter for malformed

     try: #try to open the file, and if it fails, return an error
         fs = open(fname)
     except:
         raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

     for h, line in enumerate(fs): #for each line in the file
         if line.startswith("#"): #if the file is a header
             try: 
                 if line.startswith("##FORMAT"): #if its one of the first format headers
                     fields = line.split("=<")[1].rstrip(">\r\n") + "," #separate out based on =< and "," and remove >\r\n from the end
                     i = 0 #counter
                     start = 0 #counter
                     in_string = False #boolian for string
                     while i < len(fields): #while the iteration is less than the number of fields
                         if fields[i] == "," and not in_string: #if the field is not in a string
                             name, value = fields[start:i].split('=') #separate it by =
                             if name == "ID": #if the name is ID
                                 ID = value #save the number value as ID
                             elif name == "Description": #else if the name is Description
                                 desc = value #save the value as the description value
                             start = i + 1 #initialize and add to the start counter
                         elif fields[i] == '"': #if fields is a string
                             in_string = not in_string #make it not a string
                         i += 1 #add one to the counter i
                     format_description[ID] = desc.strip('"') #format ID to be within ''
                 elif line.startswith("##INFO"): #if its not a format header, and if it is an info header
                     fields = line.split("=<")[1].rstrip(">\r\n") + "," #split the lines
                     i = 0 #reset counter
                     start = 0 #reset counter
                     in_string = False #boolian for string
                     while i < len(fields): #while i is less than the number of fields
                         if fields[i] == "," and not in_string: #if the field is a comma and is not a string
                             name, value = fields[start:i].split('=') #assign names and values
                             if name == "ID": #if its the ID
                                 ID = value #assign ID value
                             elif name == "Description": #if its the description value
                                 desc = value #assign desc value
                             elif name == "Type": #if it is the type
                                 Type = value #assign type value
                             start = i + 1 #add to the counter
                         elif fields[i] == '"': #if it is a string
                             in_string = not in_string #make it not a string
                         i += 1 #add to the i counter
                     info_description[ID] = desc.strip('"') #make the info desc within ''
                     info_type[ID] = Type #make the info type = type
                 elif line.startswith('#CHROM'): #if it is a #CHROM header
                     fields = line.lstrip("#").rstrip().split("\t") #separate by tab
                     vcf.append(fields) #append values to vcf
             except:
                 raise RuntimeError("Malformed header") #error
         else: #if its not a header
             try: #try
                 fields = line.rstrip().split("\t") #separate by tab
                 fields[1] = int(fields[1]) #convert values to integers in the first field
                 if fields[5] != ".": #if the value is present
                     fields[5] = float(fields[5]) #make it a float
                 info = {} #make a dictionary
                 for entry in fields[7].split(";"): #for every entry in the 7th column, separate them by ;
                     temp = entry.split("=") #split by =
                     if len(temp) == 1: #if length of temp is == 1 (one list)
                         info[temp[0]] = None #then it is empty
                     else: #if its not == 1
                         name, value = temp #save the name and value
                         Type = info_type[name] #save the type
                         info[name] = type_map[Type](value) #save the info
                 fields[7] = info #replace the 7th field with the new dictionary
                 if len(fields) > 8: #if the length of fields is greater than 8
                     fields[8] = fields[8].split(":") #split the 8th field by :
                     if len(fields[8]) > 1: #if there is more than one thing in field 8
                         for i in range(9, len(fields)): #for each thing in the field
                             fields[i] = fields[i].split(':') #split it by :
                     else: #if its not greater than 1
                         fields[8] = fields[8][0] #its equal to the first value
                 vcf.append(fields) #add to the vcf list
             except: #if it doesnt work
                 malformed += 1 #add to the malformed counter
     vcf[0][7] = info_description #save the info description to the vcf
     if len(vcf[0]) > 8: #if the vcf's first value is greater than 8
         vcf[0][8] = format_description #add the 8 format_description
     if malformed > 0: #if there are malformed lines
         print(f"There were {malformed} malformed entries", file=sys.stderr) #print how many there were
     return vcf #return vcf

 if __name__ == "__main__":
     fname = sys.argv[1]
     vcf = parse_vcf(fname)
     for i in range(10):
         print(vcf[i]) #print out the first 10 lines of VCF
		 
		 
#Exercise 2

 #I tried :'(

import sys

import vcfParser

fname = sys.argv[1]
vcf = vcfParser.parse_vcf(fname)
print(vcf)

fname1 = sys.argv[2]
vcf1 = vcfParser.parse_vcf(fname)
print(vcf1)
 