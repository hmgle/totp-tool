#!/usr/bin/python3

import os
from urllib import parse
import subprocess


if __name__ == '__main__':
    otppaht = os.path.expanduser('~/.otpauth/otpauth.data')
    with open(otppaht, 'r') as otpfile:
        url = otpfile.readline()
        while url:
            optdict = dict(parse.parse_qsl(parse.urlsplit(url).query))

            print(optdict)
            subprocess.run(['oathtool', '--totp', '-b', optdict['secret'].strip()])

            url = otpfile.readline()

