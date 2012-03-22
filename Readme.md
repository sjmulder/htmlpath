htmlpath
========

Command-line utility to perform XPath queries on HTML or XML documents.

Usage
-----

    usage: htmlpath [-h] expression [file]

    positional arguments:
      expression  an XPath expression
      file        an HTML or XML file (defaults to stdin)
    
    optional arguments:
      -h, --help  show this help message and exit

Optional installation:

    ln -s /path/to/htmlpath.py /usr/bin/htmlpath 

Dependencies
------------

 * Python 2.7 (other versions may work, too)
 * [Scrapy](http://scrapy.org/) to do the parsing

