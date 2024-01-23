import os
import random
import csv

running=True

def check_dir():
    if os.listdir("temp_uploads/") == []:
        return False
    else:
        return True

def get_file_data(new_file):
    with open('db/temp_image.csv') as file:
        reader = csv.reader(file)
        new_data = next(reader)
    file.close()
    new_file[1]=new_data[0]
    new_file[2]=new_data[1]
    new_file[3]=new_data[2]
    return new_file
    
def name_gen(name):
    file_type=name.split(".")[-1]
    char_set="0123456789abcdefghijklmnopqrstuvwxyz"
    unique=True
    while(unique):
        unique=False
        name=''
        for i in range(32):
            name=name+random.choice(char_set)
        name=name+"."+file_type
        try:
            with open('db/images.csv', 'rt') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    if(name == row[1]):
                        unique=True
        except(KeyError):
            print(KeyError)
        file.close()
    return name
        
def post_gen():
    new_file=[None,None,None,None]
    new_file=get_file_data(new_file)
    old_name=new_file[1]
    new_file[1]=name_gen(new_file[1])
    with open('db/images.csv', 'r') as file:
        id = int([[x.strip() for x in line.strip().split(',')] for line in file.readlines()][-1][0])
        new_file[0]=id+1
    file.close()
    with open('db/images.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(new_file)
    file.close()
    os.system("mv "+old_name+" content/images/"+new_file[1]+" &&  sed -i '1d' db/temp_image.csv")

while(running):
    os.system("sleep 5")
    if check_dir():
        post_gen()
    
    