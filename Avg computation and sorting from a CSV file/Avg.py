import csv
# For the average
from statistics import mean 
from collections import OrderedDict
def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        data=list(csv.reader(f))
        average=OrderedDict()
        for row in data :
            these_grades=[]
            name=row[0]  
            for grade in row[1:] :
                these_grades.append(float(grade))
            average[name]=mean(these_grades)
        writer =csv.writer(open(output_file_name,'w'),lineterminator='\n')  
        for row in average :
            writer.writerow([row,average[row]])        
def calculate_sorted_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        data=list(csv.reader(f))
        average=OrderedDict()
        for row in data :
            these_grades=[]
            name=row[0]  
            for grade in row[1:] :
                these_grades.append(float(grade))
            average[name]=mean(these_grades)
        average_sort=sorted(average.items(), key = lambda x : x[1])
        average1=OrderedDict()
        for letter in average_sort :
            average1[letter[0]]=letter[1]
        writer =csv.writer(open(output_file_name,'w'),lineterminator='\n')  
        for row in average1 :
            writer.writerow([row,average1[row]])
def calculate_three_best(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        data=list(csv.reader(f))
        average=OrderedDict()
        for row in data :
            these_grades=[]
            name=row[0]  
            for grade in row[1:] :
                these_grades.append(float(grade))
            average[name]=mean(these_grades)
        average_sort=sorted(average.items(), key = lambda x : x[1])    # average sort is a list
        average1=OrderedDict()
        for letter in average_sort :
            average1[letter[0]]=letter[1]
        writer =csv.writer(open(output_file_name,'w'),lineterminator='\n')  
        top3=list(reversed(list(average1.keys())))
        top3=top3[0:3]
        average=OrderedDict()     # we need a dictionary and we dont need to average so i choose it again
        for letter in top3 :
            average[letter]=average1[letter]
        for row in average :
            writer.writerow([row,average[row]])
def calculate_three_worst(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        data=list(csv.reader(f))
        average=OrderedDict()
        for row in data :
            these_grades=[]
            name=row[0]  
            for grade in row[1:] :
                these_grades.append(float(grade))
            average[name]=mean(these_grades)
        average_sort=sorted(average.items(), key = lambda x : x[1])    # average sort is a list
        average1=OrderedDict()
        for letter in average_sort :
            average1[letter[0]]=letter[1]
        writer =csv.writer(open(output_file_name,'w'),lineterminator='\n')  
        bottom3=list(average1.keys())
        bottom3=bottom3[0:3]
        average=OrderedDict()
        for letter in bottom3 :
            average[letter]=average1[letter]
        for row in average :
            writer.writerow([average[row]])
def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name,'r') as f :
        data=list(csv.reader(f))
        average=OrderedDict()
        for row in data :
            these_grades=[]
            name=row[0]  
            for grade in row[1:] :
                these_grades.append(float(grade))
            average[name]=mean(these_grades)
        median=mean(list(average.values()))
    q=open(output_file_name,'w')
    x=str(median)
    x=x.strip()
    q.write(x)
    q.close() 
 
   

    