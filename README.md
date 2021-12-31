# NorMatrix
check some norm for you

## checks :

- [x] 80 cols per line
- [x] space/tab alone (in a line)/(at the end of line)
- [x] two newline at end of file
- [x] two newline between function (between all buf chhhtt)
- [x] libc function call (pr welcome to add some libc function always banned)
- [x] nested branch more than 3 branch
- [ ] ...

## example if you run it as a github workflow
this is not the latest normatrix but :
[link](https://github.com/Saverio976/NorMatrix/runs/4674073068?check_suite_focus=true)

## run it as a github workflow
in the repo root :
```bash
mkdir .github
mkdir .github/workflows
echo "
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
      run: make -C NorMatrix/ PATH_CHECK=$PWD
" > .github/workflows/normatrix_check.yml
```

### thanks

chempa for his sample of file that dont follow the epitech norm
