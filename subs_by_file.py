import sys
from base64 import urlsafe_b64encode

def read_substitution(filename, encode):
    if encode:
        with open(filename, "rb") as fh:
            return urlsafe_b64encode(fh.read()).decode('ascii')
    else:
        with open(filename, "rt", encoding="utf-8") as fh:
            return fh.read()

def do_substitution(infilename, pattern, replacement):
    with open(infilename, "rt", encoding="utf-8") as fh:
        newText=fh.read().replace(pattern, replacement)
        return newText

def write_back(filename, content):
    with open(filename, "wt", encoding="utf-8") as fh:
        fh.write(content)

if __name__=="__main__":
    in_file = sys.argv[1]
    pattern = sys.argv[2]
    replacement_file = sys.argv[3]
    encode=False
    if len(sys.argv)>4:
        if sys.argv[4]=='-b':
            encode=True
    print(f"Replacing {pattern} in {in_file} by contents of {replacement_file}", file=sys.stderr)
    replacemnt = read_substitution(replacement_file, encode)
    substituted = do_substitution(in_file, pattern,replacemnt)
    write_back(in_file, substituted)

