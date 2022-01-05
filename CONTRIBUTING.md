# CONTRIBUTE

## add a file in the src/ folder

### file requirements:

- this file must have perms to be executable

- have a shebang on the first line
for bash :
```bash
#!/bin/bash
```
for python :
```py
#!/usr/bin/env python3
```
and other ... (search the right sheang for your file language)

- take the first parameter of argv as the file source to check
for bash :
```bash
FILE=$1
```
for python :
```
import sys
file = sys.argv[1]
```

- return 0 if there is no error

- return x if there is x error

## it is done ?
you can now create a pull request !

## thanks to help!
