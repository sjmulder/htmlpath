#!/usr/bin/env python

import sys
import codecs
from argparse        import ArgumentParser, FileType
from scrapy.http     import TextResponse
from scrapy.selector import XPathSelector

parser = ArgumentParser(description = "Perform an XPath query on an HTML or XML document.")
parser.add_argument("expression",
                    help = "an XPath expression")
parser.add_argument("file",
                    help    = "an HTML or XML file (defaults to stdin)", 
                    nargs   = "?",
                    type    = FileType('r'), 
                    default = sys.stdin)

args     = parser.parse_args() 
response = TextResponse(args.file.name, body = args.file.read(), encoding = "utf-8")
selector = XPathSelector(response)

for result in selector.select(args.expression):
	print result.extract()

