import re 
from datetime import datetime

def analyze_log(logfile):
    errorcount = 0
    warningcount = 0
    criticalerror = []

    with open(logfile , 'r') as file:
        for line in file:
            if "Error" in line:
                errorcount += 1
                if "Memoryerror" in line or "outofcontexterror" in line:
                    criticalerror.append(line.strip())
            elif "Warning" in line:
                warningcount += 1

    print(f"Total Errors: {errorcount}")
    print(f"Total Warnings: {warningcount}")    

    
    if criticalerror:
      print("Critical Errors:")
      for error in criticalerror:
        print(error)


analyze_log('errorlog.txt')
