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
#### 1
```bash
pip install normatrix
```
Now you can use it with `python3 -m normatrix` in your terminal

#### 2
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

#### 3
to update it, you just have to run
```bash
pip install -U normatrix
```

#### 4
to uninstall it (sad), run
```bash
pip uninstall normatrix
```
</details>

<details>
  <summary>From source</summary>

### from source
#### 1
```bash
git clone https://github.com/Saverio976/NorMatrix.git
cd NorMatrix
```
Now you can use it with `./path/to/folder/NorMatrix/main.py` in your terminal

#### 2
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
#### 3
to update it, just go where you have cloned normatrix
run
```bash
git pull
```

#### 4
to uninstall it (sad)
Delete the folder
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
    --conf                [deprecated] tells if you have a .normatrix config file
    --only-error          print only bad files with errors
    --output format       tell which output format to use [html, md, term_color]; for html the file is normatrix-result.htmk; for md the file is
                          normatrix-result.md

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
    --conf                [deprecated] tells if you have a .normatrix config file
    --only-error          print only bad files with errors
    --output format       tell which output format to use [html, md, term_color]; for html the file is normatrix-result.htmk; for md the file is
                          normatrix-result.md

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
    --conf                [depreacted] tells if you have a .normatrix config file
    --only-error          print only bad files with errors
    --output format       tell which output format to use [html, md, term_color]; for html the file is normatrix-result.htmk; for md the file is
                          normatrix-result.md

source: https://github.com/Saverio976/NorMatrix
```
</details>

<details>
  <summary>(only from source) Makefile (deprecated)</summary>

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
you can now configure what extension file are banned, and what are not,

all you have to do is put a file `.normatrix.json` where you execute `normatrix`

example with nothing banned and no preview (preview = not stable check) check
`.normatrix.json`
```json
{
    "banned": [],
    "no-banned": [],
    "extension": [],
    "no-extension": [],
    "enable-preview": false
}
```

just add inside `[]` the string of what you want

**other explanation with example**

<details>
  <summary>other explanation with example</summary>

- to no-banne memset (because you can use it)
```json
{
    "no-banned": ["memset"]
}
```
- to banne my_printf (because you dont want to use it)
```json
{
    "banned": ["my_printf"]
}
```
- to no-banne \*.o file (because you dont need this warning)
```json
{
    "no-extension": [".o"]
}
```
- to banne \*.c file (because you want c fiel banned)
```json
{
    "extension": [".c"]
}
```
- to enable preview check by default
```json
{
    "enable-preview": true
}
```
</details>

by default there are somthing like this:
```json
{
    "banned": ["printf", "memset", "strcpy", "strcat", "calloc"],
    "no-banned": [],
    "extension": [".a", ".o", ".so", ".gch", "~", "#", ".d"],
    "no-extension": [],
    "enable-preview": false
}
```
this configuration will be added even if you add a `.normatrix.json` file

but if you want to remove `*.o`, just add it to the `no-extension`

or you can put `*.o` in a `.gitignore`

it will remove it from the default

## example if you run it as a github workflow
this is not the latest normatrix but :

link : [link](https://github.com/Saverio976/NorMatrix/runs/5523744737?check_suite_focus=true)

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
-    and invisble testers that says **"bha baah normatrix have a bug"**

### contributors
![Contributor](https://badges.pufler.dev/contributors/Saverio976/NorMatrix?size=50&padding=5&bots=true)
