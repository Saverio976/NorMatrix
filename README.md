# NorMatrix
check some norm for you

![ubntu-latest , windows-latest, macos-latest, (python3.7, python3.8, python3.9, python3.10)](https://github.com/Saverio976/NorMatrix/actions/workflows/hallo_doctor.yml/badge.svg?event=push)
[![NorMatrix Check](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml/badge.svg)](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml)

## install:
### with pipy
```bash
pip install normatrix
```
```bash
echo $SHELL
```
if you are using bash shell (the `echo` print /something/bash):
```bash
echo alias normatrix="python -m normatrix" >> $HOME/.bashrc
```
else if you are using zsh shell (the `echo` print /something/like/zsh):
```bash
echo alias normatrix="python -m normatrix" >> $HOME/.zshrc
```
else handle this yourself bruh;
now you can just write `normatrix` on your shell

### from source:
```bash
git clone https://github.com/Saverio976/NorMatrix.git
cd NorMatrix
```
```bash
echo $SHELL
```
if you are using bash shell (the `echo` print /something/bash):
```bash
echo alias normatrix="$PWD/main.py" >> $HOME/.bashrc
```
else if you are using zsh shell (the `echo` print /something/like/zsh):
```bash
echo alias normatrix="$PWD/main.py" >> $HOME/.zshrc
```
else handle this yourself bruh;
now you can just write `normatrix` on your shell

## Current Checks :

- [x] 80 cols per line
- [x] space/tab alone (in a line)/(at the end of line)
- [x] two newline at end of file
- [x] two newline between function (between all buf chhhtt)
- [x] libc function call (pr welcome to add some libc function always banned)
- [x] nested branch more than 3 branch
- [x] no more than 20 lines per function
- [x] comma with no space after
- [x] end of parenthesis with a open curly bracket next `){`
- [x] star char `*` like this `char* buf`
- [x] preprocessors indentations (`#if..`, `#endif`)
- [x] multiple statements
- [x] 5 functions per file
- [x] filename of source code only snake\_case
- [ ] ...

## example if you run it as a github workflow
this is not the latest normatrix but :
[link](https://github.com/Saverio976/NorMatrix/runs/4743596186?check_suite_focus=true)
[![NorMatrix Check](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml/badge.svg)](https://github.com/Saverio976/NorMatrix/actions/workflows/normatrix_check.yml)
(this workflow pass well, but it will not if you copy the code below)

## doc
### (if you use pipy) python -m normatrix
```
USAGE:
	python -m normatrix [tests\_run]
DESCRIPTION:
	check the norm! in the current working directory
ARGS:
	NO		check the norm
	tests_run	run internal tests of NorMatrix
```
### (only from source) main.py
```
USAGE:
	./main.py [tests\_run]
DESCRIPTION:
	check the norm! in the current working directory
	(import normatrix.source.main and execute the main() func)
ARGS:
	NO		check the norm
	tests_run	run internal tests of NorMatrix
```
### (only from source) exec.sh
(this file exists only to keep compatibility to older version)
```
USAGE
	./exec.sh [tests\_run]
DESCRIPTION:
	check the norm! in the current working directory
	(call main.py)
ARGS:
	NO		check the norm
	tests_run	run internal tests of NorMatrix
```
### (only from source) Makefile
(this file exists only to keep compatibility to older version)
```
USAGE:
	make -C path/to/NorMatrix PATH_CHECK=$PWD
DESCRIPTION:
	check the norm! in the current working directory
	(call main.py)
ARGS:
	-C path/to/NorMatrix 	run the makefile that is in path/to/NorMatrix
				instead of the one where you are

	PATH_CHECK=$PWD		check the norm in your current working
				directory
```

## run it as a github workflow
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

    - name: clone NorMatrix
      run: git clone https://github.com/Saverio976/NorMatrix.git

    - name: NorMatrix
      run: ./NorMatrix/main.py
' > .github/workflows/normatrix_check.yml
```

## Contribute
[more information on [CONTRIBUTNG.md](https://github.com/Saverio976/NorMatrix/blob/python-rewrite/CONTRIBUTING.md)]

### thanks
chempa for his sample of file that dont follow the epitech norm
