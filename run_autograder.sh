#!/bin/bash

cp /autograder/submission/test.txt /autograder/source/test.txt

cd /autograder/source

python3 run_tests.py
