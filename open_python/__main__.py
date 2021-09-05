from optparse import OptionParser # use optparse for compatibility
from open_python import start


if __name__ == '__main__':
    parser = OptionParser("usage: %prog [options] arg")
    parser.add_option('-a', '--application', dest='application', default=None, help='application used to open the given content')
    opt, args = parser.parse_args()
    if len(args) != 1:
        parser.error('incorrect number of arguments')
    start(args[0], opt.application)
