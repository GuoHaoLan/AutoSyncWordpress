# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from subprocess import (PIPE, Popen)
import os
import json



def System(command):
    '''
    Invoke command as a new system process and return its output.
    '''
    return Popen(command, stdout=PIPE, shell=True).stdout.read()

if __name__ == "__main__":
	result = json.loads(System('curl -s -H "Cache-Control: no-cache" https://api.wordpress.org/core/version-check/1.7/?locale=zh_CN'))
	version = result['offers'][0]['version']
	download = result['offers'][0]['download']
	file = open('wpversion.txt','r')
	if os.path.exists('wpversion.txt'):
		file = open('wpversion.txt','r')

		if version != file.read():
			System('wget -O /data/home/wordpress/latest.zip {}'.format(download))
			file.close()
			file = open('wpversion.txt','w')
			file.write(version)
	else:
		file = open('wpversion.txt','w')
		file.write(version)
		if os.path.exists('/data/home/wordpress/latest.zip'):
			os.remove('/data/home/wordpress/latest.zip')
		System('wget -O /data/home/wordpress/latest.zip {}'.format(download))
		

	file.close()





