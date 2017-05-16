#!/usr/bin/env python


def test(**kwargs):
	c = kwargs
	#print c['sal']
	#print c['tom']
	for f in c:
		if f == 'tom':
			print c[f]	


def main():

	# DICTIONARY DEF
	sample = {'sal' : 0, 'tom' : 99}
	test(**sample)

	# LIST DEFINITION	
	w = ["5,6,7,8"]
	print type(w)


	
main()

# END  MASTERS
