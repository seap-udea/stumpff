test:
	@python test.py
clean:
	@find . -name "*~" -exec rm -rf {} \;
	@find . -name '__pycache__' -type d | xargs rm -fr

