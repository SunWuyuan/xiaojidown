from python:latest
 
workdir /draw_quad
 
copy requirements.txt requirements.txt
run pip install -r requirements.txt 
 
copy . .
 
cmd [ "python", "main.py"]