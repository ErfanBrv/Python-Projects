import hashlib
import csv
from collections import OrderedDict
def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        password=OrderedDict()
        data=csv.reader(f)
        for row in data :
            these_ramz=[]
            name=row[0]
            for ramz in row[1:] :
                these_ramz.append(ramz) 
            password[name]=these_ramz[0]
    hash_code=password.values()
    hash_code=list(hash_code) # i seperate the hash code from the name of the main example csv file up to now
    totall_hash=OrderedDict() #
    final=OrderedDict()
    for i in range (1000,10000) :
        totall_hash[str(i)]=  hashlib.sha256(str(i).encode('utf-8')).hexdigest()
    for letter in password :
        for letter1 in totall_hash :
            if password[letter]==totall_hash[letter1]:
                final[letter]=letter1
    writer=csv.writer(open(output_file_name,'w'),lineterminator='\n')
    for row in final :
        writer.writerow([row,final[row]])


   



