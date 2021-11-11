# NorMatrix
check some norm for you

## checks :
[x] 80 cols per line
[~] trailing space
[~] trailing newline
[~] useless file
[x] libc function call
[ ] ...

## run it as a github workflow
in the repo root : 
```bash
mkdir .github
mkdir .github/workflows
echo "
name: Norm Check

on: [push]

jobs:
  norm:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: clone NorMatrix
      run: git clone https://github.com/Saverio976/NorMatrix

    - name: NorMatrix
      run: NorMatrix/main.sh
" > .github/workflows/norm_check.yml
```
