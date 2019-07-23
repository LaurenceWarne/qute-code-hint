#!/usr/bin/env python3

import os
import html
import re
import sys
import xml.etree.ElementTree as ET


def parse_text_content(element):
    root = ET.fromstring(element)
    text = ET.tostring(root, encoding="unicode", method="text")
    text = html.unescape(text)
    return text


def main():
    delimiter = sys.argv[1] if len(sys.argv) > 1 else ";"
    # For info on qute environment vairables, see
    #https://github.com/qutebrowser/qutebrowser/blob/master/doc/userscripts.asciidoc
    element = os.environ.get("QUTE_SELECTED_HTML")
    code_text = parse_text_content(element)
    code_text = re.sub("(\n)+", delimiter, code_text)
    code_text = code_text.replace("'", "\"")
    with open(os.environ.get("QUTE_FIFO"), "w") as f:
        f.write("yank inline '{code}'\n".format(code=code_text))


if __name__ == "__main__":
    main()
