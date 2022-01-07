# CONTRIBUTE

## add a file in the plugged/ folder

### file requirements:
- have a function named `check` that take a source.file\_parser.CFileParse object
as parameter

- this function return a tuple :
first the number of error in the file
second the type of error (0 for major, 1 for minor, 2, for info)

## example
```py
from source.file_parser import CFileParse
from source.file_parser import TypeLine

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    return (nb_error, 0) 
```

## it is done ?
you can now create a pull request !

## thanks to help!
