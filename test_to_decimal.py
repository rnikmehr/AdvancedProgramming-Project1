#!/usr/bin/env python3
"""Module documentation goes here
"""

import string
import subprocess
import sys

class TestToDecimal:
    """Class to test a student app.
    """
    def __init__(self, test_no):
        self._app = "./program1"  # name of child proc
        self._test_no = test_no  # mapping to test info below
        self._input = ["11001 2", "132 8", "-112 7", "105 16","130 2"]  # test input for child proc
        self._expected = [  # expected output from child proc
            "25", "90", "-58", "Base Not Accepted", "Invalid Digit(s) In Number"]

        self.test()


    def test(self):
        """Method is called by constructor. It is public, but should not need be
        called explicitly.
        """
        returncode, actual = self._run()

        # remove all non-printable characters
        actual = "".join(filter(lambda x: x in string.printable, actual))

        if returncode != 0:
            print(
                "ERROR: EXPECTED return 0, ACTUAL return {}".format(returncode),
                file=sys.stderr)

        if not actual:
            print("ERROR: No output from student app.", file=sys.stderr)
            sys.exit(1)

        print("STUDENT OUTPUT")
        print("\t----------------------------------")
        print(f"\t  {actual}")  # this is known as an fstring
        print("\t----------------------------------")

        if actual == self._expected[self._test_no] or actual == self._expected[self._test_no] + "\n":
            print("CORRECT!")
        else:
            print("INCORRECT...")
            print(f"  Expected:\t{self._expected[self._test_no]}")
            print(f"  Actual:\t{actual}")
            sys.exit(1)


    def _run(self):
        """Does the actual work of running the tested app. Called by test method
        and returns the exit code of app and anything in STDOUT.
        """
        with subprocess.Popen(
                self._app, stderr=subprocess.PIPE,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
            out, _ = proc.communicate(
                input=self._input[self._test_no].encode("utf-8"))

            try:
                return proc.returncode, out.decode("utf-8") if out else None
            except UnicodeDecodeError as decode_exception:
                return proc.returncode, \
                       "ERROR! {}".format(decode_exception)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: test_to_decimal.py [1 | 2 | 3 | 4 | 5] to run tests 1, 2, 3, 4 or 5")
    else:
        TestToDecimal(int(sys.argv[1]) - 1)
