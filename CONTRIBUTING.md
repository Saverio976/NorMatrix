# CONTRIBUTE

## add a file in the plugged/ folder

### file requirements
-   have a function named `check` that take a source.file\_parser.CFileParse object
as parameter

-   this function return a tuple :
first the number of error in the file
second the type of error (0 for major, 1 for minor, 2 for info)

-   example
```py
try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
except:
    from normatrix.normatrix.source.file_parser import CFilePar
    from normatrix.normatrix.source.config import TypeLine

def check(file: CFileParse) -> (int, int):
    nb_error = 0
    return (nb_error, 0) 
```

## add the file name without the .py in the list in the file \_\_init\_\_.py
`normatrix/normatrix/plugged/__init__.py`
```py
__all__ = [
    "columns",
    ....,
    "your_new_filename_here"
]
```

## it is done
you can now create a pull request !

## thanks to help
