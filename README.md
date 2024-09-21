# b64

## What is this?
Python script to encode and decode base64 in command line

## Usage
```
python main.py -h
```
You can do thing like this*:<br>
```python main.py -e "some text" -q True | python main.py -d```<br>
And this*:<br>
```python main.py -e "some text" -q True | python main.py -q True -d | python main.py -e```<br>
And this*:<br>
```python main.py -q True -e "some text" > text.txt```<br>
```python main.py -q True -d < text.txt```

### Why?
Why not?

*__Example for GNU/Linux and may not work on Windows__
