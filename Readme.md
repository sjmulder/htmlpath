htmlpath
========

Command-line utility to perform XPath queries on HTML or XML documents.

Example
-------

    $ htmlpath somefile.html //a/@href
    http://foo.example.com

Usage
-----

    usage: htmlpath [-h] [file] expression

    positional arguments:
      file        an HTML or XML file (defaults to stdin)
      expression  an XPath expression
    
    optional arguments:
      -h, --help  show this help message and exit

Optional installation:

    ln -s /path/to/htmlpath.py /usr/bin/htmlpath 

Dependencies
------------

 * Python 2.7 (other versions may work, too)
 * [Scrapy](http://scrapy.org/) to do the parsing

