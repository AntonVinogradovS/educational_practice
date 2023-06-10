import concurrent.futures
import os
import subprocess

comands = ["python C:\\Users\\rusan\\AppData\\Local\\Programs\\Python\\Python311\work\\diplom\\testProcc.py 1",
           "python C:\\Users\\rusan\\AppData\\Local\\Programs\\Python\\Python311\work\\diplom\\testProcc.py 2", 
           "python C:\\Users\\rusan\\AppData\\Local\\Programs\\Python\\Python311\work\\diplom\\testProcc.py 3",
           "python C:\\Users\\rusan\\AppData\\Local\\Programs\\Python\\Python311\work\\diplom\\testProcc.py 4", 
           "python C:\\Users\\rusan\\AppData\\Local\\Programs\\Python\\Python311\work\\diplom\\testProcc.py 5"]

processes = []
for command in comands:
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

for process in processes:
    process.wait()