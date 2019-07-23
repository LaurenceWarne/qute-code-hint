# Qute Code Hint

A small qutebrowser userscript for copying code snippets on web pages to the clipboard.

## Example

Hinting:
![Hinting](https://i.imgur.com/5IBpFfO.png)

Copying to clipboard:
![Copying](https://i.imgur.com/ys9tjpt.png)

## Installation

1. Download the script:

```
wget https://raw.githubusercontent.com/LaurenceWarne/qute-code-hint/master/code_select.py -O ~/.local/share/qutebrowser/userscripts/code_select.py
```

2. In your qutebrowser config file create a new custom group for code:

```
c.hints.selectors["code"] = [
    # Selects all code tags whose direct parent is not a pre tag
    ":not(pre) > code",
    "pre"
]
```

3. Bind the userscript using a keybinding of your choice:

```
...
'<ctrl-#>': 'hint code userscript code_select.py',
...
```

4. Optionally install the python [pyperclip](https://github.com/asweigart/pyperclip) module for better multiline copying:

```
pip3 install pyperclip --user
```

### Multiline Copying
Without pyperclip the default behaviour for code snippets spanning multiple lines is to join them all on one line, with semicolons separating the previously seperate lines.
