# -*- coding: utf-8 -*-

import csv
import os
from datetime import datetime, date
from slugify import slugify
from pymongo import MongoClient

# Connect to default local instance of mongo
client = MongoClient()

# Get database and collection
db = client.undpkosovomosaic
collection = db.mosaic
collection.remove({})

def parse():

    print "Importing UNDP KOSOVO MOSAIC DATA."

    with open('data/Mosaic-2012.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_number = 0
        for row in reader:
            Q1_A = row[0]
            Q1_B = row[1]
            Q1_C = row[2]
            Q1_D = row[3]
            Q1_E = row[4]
            Q1_F = row[5]
            Q1_G = row[6]
            Q1_H = row[7]
            Q1_I = row[8]
            Q1_J = row[9]
            Q1_K = row[10]
            Q1_L = row[11]
            Q2_A = row[12]
            Q2_B = row[13]
            Q2_C = row[14]
            Q2_D = row[15]
            Q2_E = row[16]
            Q2_F = row[17]
            Q3 = row[18]
            Q4 = row[19]
            Q5_A = row[20]
            Q5_B = row[21]
            Q5_C = row[22]
            Q5_D = row[23]
            Q5_E = row[24]
            Q5_F = row[25]
            Q6 = row[26]
            Q6_jo = row[27]
            Q7 = row[28]
            Q8_A = row[29]
            Q8_B = row[30]
            Q8_C = row[31]
            Q8_D = row[32]
            Q8_E = row[33]
            Q8_F = row[34]
            Q9 = row[35]
            Q9_jo = row[36]
            Q10_A = row[37]
            Q10_B = row[38]
            Q10_C = row[39]
            Q10_D = row[40]
            Q10_E = row[41]
            Q10_F = row[42]
            Q10_G = row[43]
            Q11_A = row[44]
            Q11_B = row[45]
            Q11_C = row[46]
            Q11_D = row[47]
            Q11_E = row[48]
            Q11_F = row[49]
            Q11_G = row[50]
            Q11_H = row[51]
            Q11_I = row[52]
            Q11_J = row[53]
            Q11_K = row[54]
            Q12_A = row[55]
            Q12_B = row[56]
            Q12_C = row[57]
            Q12_D = row[58]
            Q13_A = row[59]
            Q13_B = row[60]
            Q13_C = row[61]
            Q13_D = row[62]
            Q13_E = row[63]
            Q13_F = row[65]
            Q13_G = row[66]
            Q13_H = row[67]
            Q13_I = row[68]
            Q13_J = row[69]
            Q14 = row[70]
            Q15 = row[71]
            Q15a = row[72]
            Q16 = row[73]
            Q17 = row[74]
            Q18 = row[75]
            Q19 = row[76]
            Q20 = row[77]
            Q21 = row[78]
            Q22 = row[79]
            Q23 = row[80]
            Q24 = row[81]
            Q25 = row[82]
            Q26 = row[83]

            report = {
                "data": {
                    "Q1_A    "   :   Q1_A,
                    "Q1_B"   :   Q1_B,
                    "Q1_C"   :   Q1_C,
                    "Q1_D"   :   Q1_D,
                    "Q1_E"   :   Q1_E,
                    "Q1_F"   :   Q1_F,
                    "Q1_G"   :   Q1_G,
                    "Q1_H"   :   Q1_H,
                    "Q1_I"   :   Q1_I,
                    "Q1_J"   :   Q1_J,
                    "Q1_K"   :   Q1_K,
                    "Q1_L"   :   Q1_L,
                    "Q2_A"   :   Q2_A,
                    "Q2_B"   :   Q2_B,
                    "Q2_C"   :   Q2_C,
                    "Q2_D"   :   Q2_D,
                    "Q2_E"   :   Q2_E,
                    "Q2_F"   :   Q2_F,
                    "Q3"   :   Q3,
                    "Q4"   :   Q4,
                    "Q5_A"   :   Q5_A,
                    "Q5_B"   :   Q5_B,
                    "Q5_C"   :   Q5_C,
                    "Q5_D"   :   Q5_D,
                    "Q5_E"   :   Q5_E,
                    "Q5_F"   :   Q5_F,
                    "Q6"   :   Q6,
                    "Q6_jo"   :   Q6_jo,
                    "Q7"   :   Q7,
                    "Q8_A"   :   Q8_A,
                    "Q8_B"   :   Q8_B,
                    "Q8_C"   :   Q8_C,
                    "Q8_D"   :   Q8_D,
                    "Q8_E"   :   Q8_E,
                    "Q8_F"   :   Q8_F,
                    "Q9"   :   Q9,
                    "Q9_jo"   :   Q9_jo,
                    "Q10_A"   :   Q10_A,
                    "Q10_B"   :   Q10_B,
                    "Q10_C"   :   Q10_C,
                    "Q10_D"   :   Q10_D,
                    "Q10_E"   :   Q10_E,
                    "Q10_F"   :   Q10_F,
                    "Q10_G"   :   Q10_G,
                    "Q11_A"   :   Q11_A,
                    "Q11_B"   :   Q11_B,
                    "Q11_C"   :   Q11_C,
                    "Q11_D"   :   Q11_D,
                    "Q11_E"   :   Q11_E,
                    "Q11_F"   :   Q11_F,
                    "Q11_G"   :   Q11_G,
                    "Q11_H"   :   Q11_H,
                    "Q11_I"   :   Q11_I,
                    "Q11_J"   :   Q11_J,
                    "Q11_K"   :   Q11_K,
                    "Q12_A"   :   Q12_A,
                    "Q12_B"   :   Q12_B,
                    "Q12_C"   :   Q12_C,
                    "Q12_D"   :   Q12_D,
                    "Q13_A"   :   Q13_A,
                    "Q13_B"   :   Q13_B,
                    "Q13_C"   :   Q13_C,
                    "Q13_D"   :   Q13_D,
                    "Q13_E"   :   Q13_E,
                    "Q13_F"   :   Q13_F,
                    "Q13_G"   :   Q13_G,
                    "Q13_H"   :   Q13_H,
                    "Q13_I"   :   Q13_I,
                    "Q13_J"   :   Q13_J,
                    "Q14":   Q14,
                    "Q15":   Q15,
                    "Q15a"   :   Q15a,
                    "Q16"   :   Q16,
                    "Q17"   :   Q17,
                    "Q18"   :   Q18,
                    "Q19"   :   Q19,
                    "Q20"   :   Q20,
                    "Q21"   :   Q21,
                    "Q22"   :   Q22,
                    "Q23"   :   Q23,
                    "Q24"   :   Q24,
                    "Q25"   :   Q25,
                    "Q26"   :   Q26
                }
            }
            collection.insert(report)


parse()
