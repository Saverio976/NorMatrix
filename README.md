# NorMatrix
check some norm for you

## checks :
[x] 80 cols per line

[x] trailing space

[x] trailing newline

[x] libc function call

[ ] ...

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
