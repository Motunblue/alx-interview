#!/usr/bin/python3
"""Log Parsing Module"""
import sys
import signal
import re


sCodes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
    }
file_size = 0


def write_out():
    print("File size: {:d}".format(file_size))
    for k, v in sCodes.items():
        if v > 0:
            print("{}: {}".format(k, v))
            sCodes[k] = 0


def sigint_handler(signum, frame):
    write_out()


signal.signal(signal.SIGINT, sigint_handler)

count = 0

for line in sys.stdin:
    pat1 = r"^(([0-9]{1,3}\.){3}[0-9]{1,3})\s+-\s+\[(\d{4}-\d{2}-\d{2}.+)\]\s+"
    pat2 ="\"GET\s+/projects/260 HTTP/1.1\"\s+(\d{3})\s+(\d+)$"
    pat = pat1 + pat2
    match = re.match(pat, line)
    if not match:
        continue
    ip, _, date, status, size = match.groups()
    if status not in sCodes.keys():
        continue
    count += 1
    file_size += int(size)
    sCodes[status] += 1
    if count == 10:
        write_out()
        count = 0
