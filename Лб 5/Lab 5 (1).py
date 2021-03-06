import csv
import os
import random
import shutil

def read(filename):
    fd = open(filename, "r")
    reader = csv.reader(fd, delimiter = "\t")
    for row in reader:
        print(row)
    fd.close()
    print("зчитування файлу виконано")

def write(filename):
    fd = open(filename, "w")
    for i in range(8):
        A = i*17
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("запис файлу виконано")

def append(filename): 
    fd = open(filename, "a")
    for i in range(17):
        A = random.uniform(2, 5)
        fd.write("%i\t%.1f\n" % (i, A))
    fd.close()
    print("дозапис у кінець файлу виконано") 

def rename(filename):
    os.rename("F:\ICS-485773\ICS-485773\Лб 5\mydirectorya.txt")
    print("перейменування файлу виконано") 

def delete(filename):
    os.remove("F:\ICS-485773\ICS-485773\Лб 5\mydirectorya.txt")
    print("видалення файлу виконано")
     
def copy(filename):
    shutil.copyfile("F:\ICS-485773\ICS-485773\Лб 5\mydirectorya.txt", "F:\ICS-485773\ICS-485773\Лб 5\mydirectorya(2).txt")
    print("копіювання файлу виконано") 

filename = "mydata.txt"
x=int(input("виберіть режим роботи з файлом: \n [1] - читати з файла \n [2] - записати у файл \n [3] - дозапис у файл \n [4] - перейменувати файл \n [5] - видалити файл \n [6] - зробити копію файлу  \n"))          

mode = ' '
if x == 1:
    read(filename)
elif x == 2:
    write(filename)
elif x == 3:
    append(filename) 
elif x == 4:
    rename(filename)
elif x == 5:
    delete(filename)         
elif x == 6:
    copy(filename)
else:
    print("Немає такого варіанту")

input('Натисніть ENTER щоб вийти') 
        
