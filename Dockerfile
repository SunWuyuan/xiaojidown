from python:3.9-slim-buster
 
workdir /draw_quad
 
copy requirements.txt requirements.txt
run pip3 install -r requirements.txt 
 
copy . .
 
cmd [ "python3", "main.py"]