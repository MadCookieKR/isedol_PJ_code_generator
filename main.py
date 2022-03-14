import re

if __name__ == '__main__':
    script = open("test.txt", "r")
    newFile = open("code.txt", "w")
    for line in script.readlines():
        regex = re.compile("(.*): (.*)")
        m = regex.search(line)
        line = line.strip()
        if not line:
            continue
        if m is not None:
            speaker = m.group(1)
            content = m.group(2)
            newFile.write(f's1.Add(new Say("{speaker}", "{content}"));\n')
        else:
            newFile.write(f's1.Add(new Say("", "{line}"));\n')
    script.close()
    newFile.close()