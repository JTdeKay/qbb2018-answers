#!/usr/bin/env python3

import sys
#Making dictionary

if len(sys.argv) < 2:
    print("Enter map file < SRR file after program name")
    quit()
if len(sys.argv) <3:
    print("Enter S or U after SRR file, S skips lines without match, U prints Unknown")
    quit()
 
mapping_dict = {}

#output file pulled in by sys.argv
for line in open(sys.argv[1]):
    fields = line.rstrip("\r\n").split()
    FlyBaseID_key = fields[0]
    UniprotID_value = fields[1]
    mapping_dict[FlyBaseID_key] = UniprotID_value
#Loop to check between files   
for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split()
    FlyBaseID = fields[8]
    if FlyBaseID in mapping_dict:
        UniProtID = mapping_dict[FlyBaseID]
        print(line + "  " + UniProtID)  
        if sys.argv[2] == "U":
            print(line + "  " + "Unknown")
        if sys.argv[2] == "S":
            continue
        
            
        

        
