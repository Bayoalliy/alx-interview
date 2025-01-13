#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C),
print these statistics from the beginning:
    Total file size: File size: <total size>
    where <total size> is the sum of all previous <file size>

    Number of lines by status code
        possible status code: 200, 301, 400, 401,
        403, 404, 405 and 500

        if a status code doesn’t appear or is not an integer,
        don’t print anything for this status code

    format: <status code>: <number>
    status codes should printed in ascending order
"""
import sys
import re
import signal


dic = {
        'f_size': 0,
        }


def print_logs(dic):
    """print dic in specified format"""
    print('File size: {}'.format(dic['f_size']))
    for key, value in sorted(dic.items()):
        if key != 'f_size':
            print(f"{key}: {value}")


def handler(signum, frame):
    """handles Ctrl c Keyinterrupt"""
    print_logs(dic)


signal.signal(signal.SIGINT, handler)


def parse_line():
    """extract status code and calculates total file size"""
    st_code_patt = r"\s(200|301|400|500|404|403|405|401)\s"
    f_size_patt = r" \d+$"
    i = 1
    for line in sys.stdin:
        # get status code
        st_code = re.search(
                st_code_patt, line.strip()).group().strip()
        f_size = re.search(
                f_size_patt, line.strip()).group().strip()

        if st_code and st_code in dic:
            dic[st_code] += 1
        elif st_code and st_code not in dic:
            dic[st_code] = 1
        if f_size:
            dic['f_size'] += int(f_size)

        if i > 9 and i % 10 == 0:
            print_logs(dic)
        i += 1
    print_logs(dic)


if __name__ == '__main__':
    parse_line()
