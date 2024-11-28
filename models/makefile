make:
	python3 -m py_compile ./main.py ./dbCon.py ./paillerKeys.py ./paillerKeys.py ./vote.py ./provence.py
	mv ./__pycache__/main.cpython*.pyc ./main.out
	chmod +x ./main.out

clean:
	rm ./main.out