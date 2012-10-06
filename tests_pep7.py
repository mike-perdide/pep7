#!/usr/bin/env python
from subprocess import Popen, PIPE
import re

pep7_output_regex = re.compile("^.*?:(.*)$")


def run_pep7(filename):
    handle = Popen(["./pep7.py", filename], stdout=PIPE)
    stdout = handle.communicate()[0]

    for line in stdout.rstrip().split("\n"):
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
            'tests/returnparen.c')

for filename in filelist:
    errors = [error for error in run_pep7(filename)]
    expected_results = [expected for expected in extract_expected(filename)]

    print "=====", filename, ": ",
    print len(expected_results), "tests", "====="
    for expected in expected_results:
        assert expected in errors, \
               "The following error is missing: %s" % expected
