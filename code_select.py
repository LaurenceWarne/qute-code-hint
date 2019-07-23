#!/usr/bin/env python3

import os
import html
from html.parser import HTMLParser


class CodeParser(HTMLParser):

    def __init__(self, delimiter=";"):
        super().__init__()
        self.last_handled_data = ""
        self.delimiter = delimiter

    def handle_data(self, data):
        self.last_handled_data = html.unescape(data)
        self.last_handled_data = self.last_handled_data.replace(
            "\n", self.delimiter
        )


def main():
    element = os.environ.get("QUTE_SELECTED_HTML")
    parser = CodeParser()
    parser.feed(element)
    code_text = parser.last_handled_data
    with open(os.environ.get("QUTE_FIFO"), "w") as f:
        f.write("yank inline '{code}'\n".format(code=code_text))


if __name__ == "__main__":
    main()
