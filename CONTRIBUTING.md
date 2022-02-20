# CONTRIBUTE

## add a file in the plugged/ folder

### file requirements
-   have a function named `check` that take a `Context` and a `CFileParse` object
as parameter

-   this function return a tuple :
first the number of error in the file
second the type of error (0 for major, 1 for minor, 2 for info)

-   example
```py
try:
    from normatrix.source.file_parser import CFileParse
    from normatrix.source.config import TypeLine
    from normatrix.source.context import Context
except:
    from normatrix.normatrix.source.file_parser import CFilePar
    from normatrix.normatrix.source.config import TypeLine
    from normatrix.normatrix.source.context import Context

def check(context: Context, file: CFileParse) -> (int, int):
    nb_error = 0
    type_error = 1 # this is a minor error
    return (nb_error, type_error) 
```

## add the file name without the .py in the list in the file `normatrix/normatrix/plugged/__init__.py`
`normatrix/normatrix/plugged/__init__.py`
```py
PREVIEW = [
    ...,
    "your_new_filename_here_without_py_extension"
]
```

## it is done
you can now create a pull request !

your check will be added to the preview (only accessible with --preview)
during a certain period of time (time to use it at least one time in a rela project)
after, it will be added to defaults check if no error trigger

## thanks to help
