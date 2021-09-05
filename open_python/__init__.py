# cross-platform version of: os.startfile()

import os, sys, subprocess
import distutils.spawn
from six import string_types

def start(input_str, application='', quiet=True):

	# force input_str to be a string
	if not isinstance(input_str, string_types):
		input_str = ''

	# force application to be a string
	if not isinstance(application, string_types):
		application = ''
	
	def run(*args):
		DEVNULL = open(os.devnull, 'w')
		if quiet:
			return subprocess.call(args, stdout=DEVNULL, stderr=subprocess.STDOUT)
		else:
			return subprocess.call(args)

	# open input_str with either default application or specified application
	if sys.platform == 'darwin':
		if application == '':
			run('open', input_str)
		else:
			run('open', '-a', application, input_str)
	elif sys.platform == 'win32':
		if application == '':
			run('start', '', input_str)
		else:
			run('start', '', application, input_str)
	else:
		if application == '':
			application = distutils.spawn.find_executable("xdg-open") # default to system installation of xdg-open
			if application is None:
				raise RuntimeWarning('xdg-open not found, fallback to bundled version')
				application = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendor', 'xdg-open')
		run(application, input_str)
