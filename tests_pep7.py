#!/usr/bin/env python
from subprocess import Popen, PIPE
import re

pep7_output_regex = re.compile("^.*?:(.*)$")


def run_pep7(filename):
    handle = Popen(["./pep7.py", filename], stdout=PIPE, stderr=PIPE)
    stdout = handle.communicate()[0]

    for line in stdout.rstrip().split("\n"):
        if line.strip():
            match = pep7_output_regex.match(line)
            yield match.group(1)


def extract_expected(filename):
    recording = False
    regex = re.compile("^ \* (.*)$")
    with open(filename) as handle:
        for line in handle:
            if recording:
                match = regex.match(line)
                if match:
                    yield match.group(1)
            elif " * TESTS RESULTS:" in line:
                recording = True

filelist = ('tests/functiondefstyle.c',
            'tests/slashslash.c',
            'tests/returnparen.c',
            'tests/falsepositivewhitespaceop.c')

for filename in filelist:
    errors = set([error for error in run_pep7(filename)])
    expected_results = set([expected
                            for expected in extract_expected(filename)])

    print "=====", filename, ": ",
    print len(expected_results), "tests", "====="

    if errors - expected_results:
        print "* unexpected errors:", len(errors - expected_results)
        for error in errors - expected_results:
            print error.strip()

    if expected_results - errors:
        print "* missing errors:", len(expected_results - errors)
        for expected in expected_results:
            print expected.strip()
