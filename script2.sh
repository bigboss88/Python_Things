for i in {1..10}
do
	echo "Time $i"
	pytest tests.py -v
done
