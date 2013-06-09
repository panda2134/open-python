# open

## Description ##

    Open a file, directory, or URI using the OS's default application for
    that object type. Optionally, you can specify an application to use.

    This is a proxy for the following commands:

	        OSX: "open"
	    Windows: "start"
	Linux/Other: "xdg-open"

    This is a python port of the node.js module:
    https://github.com/pwnall/node-open


## Import ##

    import open

## Usage ##

### open google.com in the user's default browser:

	open.start("https://google.com/")

### you can specify the program to use:

	open.start("https://google.com/", "firefox")	


## License ##

Copyright (c) 2013 skratchdot  
Licensed under the MIT license.
