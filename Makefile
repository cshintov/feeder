all: test

test:
	ptw --onpass "say passed" --onfail "say failed" \
	    --runner "pytest --maxfail=5 --ff -s" \
	#--runner "pytest --testmon" \

debug:
	cd ${problem} && ptw --onpass "say passed" --onfail "say failed" \
	--runner "pytest --testmon" \
	--pdb

clean:
	find . -name '*pycache*' -exec rm -rf '{}' +;

