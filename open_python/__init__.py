# cross-platform version of: os.startfile()

import os, sys, subprocess
import distutils.spawn
from six import string_types

def start(input_str, application=''):

	# force input_str to be a string
	if not isinstance(input_str, string_types):
		input_str = ''

	# force application to be a string
	if not isinstance(application, string_types):
		application = ''

	# open input_str with either default application or specified application
	if sys.platform == 'darwin':
		if application == '':
			subprocess.call(['open', input_str])
		else:
			subprocess.call(['open', '-a', application, input_str])
	elif sys.platform == 'win32':
		if application == '':
			subprocess.call(['start', '', input_str])
		else:
			subprocess.call(['start', '', application, input_str])
	else:
		if application == '':
			application = distutils.spawn.find_executable("xdg-open") # default to system installation of xdg-open
			if application is None:
				raise RuntimeWarning('xdg-open not found, fallback to bundled version')
				application = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vendor', 'xdg-open')
		subprocess.call([application, input_str])
