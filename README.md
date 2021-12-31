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
- [ ] ...

## example if you run it as a github workflow
this is not the latest normatrix but :
[link](https://github.com/Saverio976/NorMatrix/runs/4675702867?check_suite_focus=true)

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
if you want to add some checkers, in python, or bash, add a file in src/ 
folder with a filename clear enouth. If there is one error or more, exit with
status code 1, else status code 0. You must say the file and this line if
 possible

### thanks

chempa for his sample of file that dont follow the epitech norm
