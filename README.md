# b64

## What is this?
Python script to encode and decode base64 in command line

## Usage
```
python main.py -h
```
You can do thing like this:
```
python main.py -e "some text" -q True | python main.py -d
```
And this:
```
python main.py -e "some text" -q True | python main.py -q True -d | python main.py -e
```
And this*:
```
python main.py -q True -e "some text" > text.txt
python main.py -q True -d < text.txt
```

### Why?
Why not?

* Example for GNU/Linux and may not work on Windows
