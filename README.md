# NorMatrix
check some norm for you

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
- [ ] ...

## example if you run it as a github workflow
this is not the latest normatrix but :
[link](https://github.com/Saverio976/NorMatrix/runs/4694219038?check_suite_focus=true)
(this workflow pass well, but it will not if you copy the code below)

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
      run: git clone https://github.com/Saverio976/NorMatrix

    - name: NorMatrix
      run: make -C NorMatrix/ PATH_CHECK=.
' > .github/workflows/normatrix_check.yml
```

## Contribute
if you want to add some checkers (in python, bash, or node),
add a file in src/ folder with a filename clear enouth.

if the filename is `test.sh`, the file wiil be executed like this `./src/test.sh {file to check}`

If there is one error or more, exit with the number of error, else 
status code 0. You must print the filename and the line where the error is

### thanks

chempa for his sample of file that dont follow the epitech norm
