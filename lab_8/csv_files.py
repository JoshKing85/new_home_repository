import csv

def create_csv(filename, data):
   with open(filename, mode='w', newline= '') as file:
      writer = csv.writer(file)
      writer.writerows(data)


def read_csv(filename):
   
   with open(filename, mode= 'r') as file:
      
      reader = csv.reader(file)

      for row in reader:
         print(row)
   

def append_to_csv(filename, data):
    
    with open(filename, mode='a', newline= '') as file:
       
       writer = csv.writer(file)

       writer.writerows(data)



