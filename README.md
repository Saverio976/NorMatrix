# NorMatrix
check some norm for you

![uuntu-latest , windows-latest, macos-latest, (python3.7, python3.8, python3.9, python3.10)](https://github.com/Saverio976/NorMatrix/actions/workflows/hallo_doctor.yml/badge.svg?event=push)

## install:
```bash
git clone https://github.com/Saverio976/NorMatrix.git
```

## checks :

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
(this workflow pass well, but it will not if you copy the code below)

## doc
#### main.py
```
USAGE:
	./main.py [tests\_run]
DESCRIPTION:
	check the norm! in the current working directory
ARGS:
	NO		check the norm
	tests_run	run internal tests of NorMatrix
```
#### exec.sh
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
#### Makefile
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

## run it with an alias
with this, you will can just write `normatrix` in a shell and it will check
the norm for your current working directory

if you are using bash shell:
```bash
echo alias normatrix="$PWD/main.py" >> $HOME/.bashrc
```
if you are using zsh shell:
```bash
echo alias normatrix="$PWD/main.py" >> $HOME/.zshrc
```
else, handle this yourself bruh

## Contribute
[more preicse information on the file : CONTRIBUTING.md]

### thanks
chempa for his sample of file that dont follow the epitech norm
