import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner

if __name__ == "__main__":
    print("discovering tests")
    suite = unittest.defaultTestLoader.discover("tests")
    with open("autograder/results/results.json", "w") as f:
        print("writing to output")
        JSONTestRunner(visibility="visible", stream=f).run(suite)
