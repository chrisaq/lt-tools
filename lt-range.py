#!/usr/bin/env python
from __future__ import print_function

from os import walk
import sys
from re import match

if len(sys.argv) < 2:
    sys.exit('Need range parameter, 200-900')

if not 199 < int(sys.argv[1]) < 901:
    sys.exit('Out of range, 200-900')

fsroot = '/sys/bus/hid/drivers/logitech'
try:
    ltroot = next(walk(fsroot))
except StopIteration as e:
    sys.exit('{} {}'.format('No logitech devices found in', fsroot))

for ddir in ltroot[1]:
    if match(r'\d{4}:.{4}:.{4}\.\d{4}$', ddir):
        devfiles = next(walk(fsroot + '/' + ddir))
        if 'real_id' and 'range' in devfiles[2]:
            with open(fsroot + '/' + ddir + '/' + 'real_id', 'r') as dev_id:
                if 'G27' or 'G25' in dev_id.readline():
                    # print("setting range %s" % sys.argv[1])
                    with open(fsroot + '/' + ddir + '/' + 'range', 'w') as dev_range:
                        dev_range.write(sys.argv[1])

