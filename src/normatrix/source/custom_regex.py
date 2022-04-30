import regex
import sys

def re_search(pattern: str, string: str, timeout: int = 1):
    try:
        return regex.search(pattern, string, timeout=timeout)
    except TimeoutError:
        sys.stderr.write(f"REGEX: timeout\n")
        return None

def re_sub(pattern: str, repl: str, string: str, timeout: int = 1, count = None):
    try:
        if count == None:
            return regex.sub(pattern, repl, string, timeout=timeout)
        else:
            return regex.sub(pattern, repl, string, count=count, timeout=timeout)
    except TimeoutError:
        sys.stderr.write(f"REGEX: timeout\n")
        return string

def re_match(string: str, reg_compile, timeout=1):
    try:
        return reg_compile.match(string, timeout=timeout)
    except TimeoutError:
        sys.stderr.write(f"REGEX: timeout\n")
        return None

def re_compile(pattern: str):
    return regex.compile(pattern)
