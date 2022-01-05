git clone https://github.com/Saverio976/NorMatrix

CHECKERS=`diff -q src/ NorMatrix/src/ | grep -v -e 'NorMatrix' | cut -d' ' -f4`

echo new checkers : $CHECKERS

make CHECKERS="$CHECKERS" PATH_CHECK=tests/bad_code/

if [[ $? == 0 ]]; then
	echo Why Did You Say It Is A Good Code
	exit 1
else
	exit 0
fi
