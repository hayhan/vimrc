#!/usr/bin/env python3
"""
Remove the invalid lines from compile_commands.json
"""

import re

good_entries = []
pattern_found = False

pattern0 = re.compile(r' *\"-mips32\"')
pattern1 = re.compile(r' *\"-fno-for-scope\"')

pattern_array = [
    pattern0,
    pattern1,
]

with open('compile_commands.json', 'r') as fin:
    for line in fin.readlines():
        for pattern in pattern_array:
            if pattern.match(line):
                pattern_found = True
                break
        if not pattern_found:
            good_entries.append(line)
        else:
            pattern_found = False

# Overwrite the old file with the new one
with open('compile_commands.json', 'w+') as fin:
    fin.writelines(good_entries)

