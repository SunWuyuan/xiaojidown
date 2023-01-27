from python:3.9
 
workdir /draw_quad
 
copy requirements.txt requirements.txt
run pip install -r requirements.txt 
 
copy main.py main.py
copy file.csv file.csv
 
cmd [ "python", "main.py"]