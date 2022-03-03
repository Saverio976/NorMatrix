# NorMatrix
check some norm for you

[![PyPI version](https://badge.fury.io/py/normatrix.svg)](https://badge.fury.io/py/normatrix)

![python-version](https://img.shields.io/badge/python-%3E%3D3.7-green)

![windows+ubuntu+macos;3.9,3.10](https://github.com/Saverio976/NorMatrix/actions/workflows/hallo_doctor.yml/badge.svg?event=push)

[![NorMatrix Check](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml/badge.svg)](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml)

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/2ca7ba5d6a9e4619bd0cab7ae82ae7e1)](https://www.codacy.com/gh/Saverio976/NorMatrix/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Saverio976/NorMatrix&amp;utm_campaign=Badge_Grade)

![GitHub repo size](https://img.shields.io/github/repo-size/Saverio976/NorMatrix?style=plastic)

![GitHub language count](https://img.shields.io/github/languages/count/Saverio976/NorMatrix?style=plastic)

![GitHub top language](https://img.shields.io/github/languages/top/Saverio976/NorMatrix?style=plastic)

![GitHub last commit](https://img.shields.io/github/last-commit/Saverio976/NorMatrix?color=red&style=plastic)

## install
<details>
  <summary>With Pipy</summary>

### with pipy
```bash
pip install normatrix
```
Now you can use it with `python3 -m normatrix` in your terminal

And if you want to just write `normatrix` :
```bash
echo $SHELL
```
if you are using bash shell (the `echo` print `/something/bash`):
```bash
echo alias normatrix=\"python3 -m normatrix\" >> $HOME/.bashrc
```
else if you are using zsh shell (the `echo` print `/something/like/zsh`):
```bash
echo alias normatrix=\"python3 -m normatrix\" >> $HOME/.zshrc
```
else handle this yourself bruh;
</details>

<details>
  <summary>From source</summary>

### from source
```bash
git clone https://github.com/Saverio976/NorMatrix.git
cd NorMatrix
```
Now you can use it with `./path/to/folder/NorMatrix/main.py` in your terminal

And if you want to just write `normatrix` :
```bash
echo $SHELL
```
if you are using bash shell (the `echo` print `/something/bash`):
```bash
echo alias normatrix=\"$PWD/main.py\" >> $HOME/.bashrc
```
else if you are using zsh shell (the `echo` print `/something/like/zsh`):
```bash
echo alias normatrix=\"$PWD/main.py\" >> $HOME/.zshrc
```
else handle this yourself bruh;
</details>

## Current Checks

-   [x] 80 cols per line
-   [x] space/tab alone (in a line)/(at the end of line)
-   [x] two newline at end of file
-   [x] two newline between function (between all buf chhhtt)
-   [x] libc function call (pr welcome to add some libc function always banned)
-   [x] nested branch more than 3 branch
-   [x] no more than 20 lines per function
-   [x] comma with no space after
-   [x] end of parenthesis with a open curly bracket next `){`
-   [x] star char `*` like this `char* buf`
-   [x] preprocessors indentations (`#if..`, `#endif`)
-   [x] multiple statements
-   [x] 5 functions per file
-   [x] filename of source code only snake\_case
-   [x] no line break at end of file
-   [x] 5+5 7/9 that need a space (but some false positiv goes in)
-   [x] no space after [ and space  before ]
-   [x] header
-   [x] #define in .c
-   [x] make + check exe if the compiler add some banned function
-   [ ] ...

## doc
<details>
  <summary>(if you use pipy) python -m normatrix</summary>

### (if you use pipy) python -m normatrix
```bash
usage: python -m normatrix [-h] [--no-operators-pluggin] [--preview] [--conf] [paths ...]

The C Epitech Coding Style Norm Checker

positional arguments:
  paths                 list of path to check (default: the current working directory)

  options:
    -h, --help            show this help message and exit
    --no-operators-pluggin
                          remove the operators pluggin (because it print some false positiv for now)
    --preview             add some plugin that are added recently
    --conf                tells if you have a .normatrix config file

source: https://github.com/Saverio976/NorMatrix
```
</details>

<details>
  <summary>(only from source) main.py</summary>

### (only from source) main.py
```bash
usage: python -m normatrix [-h] [--no-operators-pluggin] [--preview] [--conf] [paths ...]

The C Epitech Coding Style Norm Checker

positional arguments:
  paths                 list of path to check (default: the current working directory)

  options:
    -h, --help            show this help message and exit
    --no-operators-pluggin
                          remove the operators pluggin (because it print some false positiv for now)
    --preview             add some plugin that are added recently
    --conf                tells if you have a .normatrix config file

source: https://github.com/Saverio976/NorMatrix
```
</details>

<details>
  <summary>(only from source) exec.sh</summary>

### (only from source) exec.sh
(this file exists only to keep compatibility to older version)
```bash
usage: python -m normatrix [-h] [--no-operators-pluggin] [--preview] [--conf] [paths ...]

The C Epitech Coding Style Norm Checker

positional arguments:
  paths                 list of path to check (default: the current working directory)

  options:
    -h, --help            show this help message and exit
    --no-operators-pluggin
                          remove the operators pluggin (because it print some false positiv for now)
    --preview             add some plugin that are added recently
    --conf                tells if you have a .normatrix config file

source: https://github.com/Saverio976/NorMatrix
```
</details>

<details>
  <summary>(only from source) Makefile</summary>

### (only from source) Makefile
(this file exists only to keep compatibility to older version)
(if you can, move to another choice)
```bash
USAGE:
    make -C path/to/NorMatrix PATH_CHECK=$PWD
DESCRIPTION:
    check the norm! in the current working directory
    (call main.py)
ARGS:
    -C path/to/NorMatrix    run the makefile that is in path/to/NorMatrix
                            instead of the one where you are

    PATH_CHECK=$PWD	        check the norm in your current working
                            directory
```
</details>

### configuration
you can now configure what functions are banned, and what are not,

or add some file extension that not be present when you do a normatrix.

all you have to do is add `--conf` when execute normatrix and
put a file `.normatrix.json` where is the folder that
you want to check with this:

`.normatrix.json`
```json
{
    "banned": [],
    "no-banned": [],
    "no-extension": []
    "enable-preview": true
}
```

just add inside `[]` string of what you want

for example to no-banned memset (because you can use it)
```json
{
    "no-banned": ["memset"]
}
```

by default (and default configuration will be load before yours) there are somthing like this:
```json
{
    "banned": ["printf", "memset", "strcpy", "strcat", "calloc"],
    "no-banned": [],
    "no-extension": [".a", ".o", ".so", ".gch", "~", "#", ".d"]
    "enable-preview": false
}
```

## example if you run it as a github workflow
this is not the latest normatrix but :

link : [link](https://github.com/Saverio976/NorMatrix/runs/4843598808?check_suite_focus=true)

state : [![NorMatrix Check](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml/badge.svg)](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml)

(N.B. : this workflow pass well, but it will not if you copy the code below)

## run it as a **github workflow**
in the repo root :
```bash
mkdir .github
mkdir .github/workflows
echo '
name: NorMatrix Check

on: [push]

jobs:
  norm:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: set up python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'

    - name: clone NorMatrix
      run: git clone https://github.com/Saverio976/NorMatrix.git

    - name: NorMatrix
      run: ./NorMatrix/main.py
' > .github/workflows/normatrix_check.yml
```

## Contribute
***[more information on [CONTRIBUTNG.md](https://github.com/Saverio976/NorMatrix/blob/python-rewrite/CONTRIBUTING.md)]***

### special thanks
-    chempa for his sample of file that dont follow the epitech norm
-    and invisble testers that says "bha baah normatrix have a bug"

### contributors
![Contributor](https://badges.pufler.dev/contributors/Saverio976/NorMatrix?size=50&padding=5&bots=true)
