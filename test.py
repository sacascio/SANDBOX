#!/usr/bin/env python


def test(*args):
	return [x for x in args]


def main():
	p = 55
	q = 56
	print test(p,q)	


main()
