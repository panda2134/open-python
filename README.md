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

```python
import open_python
```

## Usage ##

### open google.com in the user's default browser:

```python
open_python.start("https://google.com/")
```
### you can specify the program to use:

```python
open_python.start("https://google.com/", "firefox")	
```

## use in command line

```sh
$ python -m open_python https://google.com/
```

## License ##

Copyright (c) 2013 skratchdot  
Licensed under the MIT license.
## Contributors ##

skratchdot
panda2134