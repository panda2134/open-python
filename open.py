# cross-platform version of: os.startfile()

import os, sys, subprocess

def start(input, application=''):

	# force input to be a string
	if not isinstance(input, basestring):
		input = ''

	# force application to be a string
	if not isinstance(application, basestring):
		application = ''

	# open input with either default application or specified application
	if sys.platform == 'darwin':
		if application == '':
			subprocess.call(['open', input])
		else:
			subprocess.call(['open', '-a', application, input])
	elif sys.platform == 'win32':
		if application == '':
			subprocess.call(['start', '', input])
		else:
			subprocess.call(['start', '', application, input])
	else:
		if application == '':
			application = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vender', 'xdg-open')
		subprocess.call([application, input])
