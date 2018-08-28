#!/usr/bin/env python3

import sys
 

for line in open( sys.argv[1] ):
    if "DROME" in line:
        fields = line.rstrip("\r\n").split()       
        if len(fields) != 4:
            continue
        else:
            FlyBase_ID = fields[3]
            Uniprot_ID_AC = fields[2]
            print(FlyBase_ID, Uniprot_ID_AC)