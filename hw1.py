# Name: ...
# Evergreen Login: Gootra28
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function availablea

###
### Problem 1
### 

print "Problem 1 solution follows:"
# I set mt vareables to the values I wanted then I entered the equations
a = 1
b = -5.86
c = 8.5408
Solution1 = (-b + math.sqrt(pow(b,2) - (4*a*c)))/(a*2)
print Solution1

Solution2 = (-b - math.sqrt(pow(b,2) - (4*a*c)))/(a*2)
print Solution2
###
### Problem 2
###

print "Problem 2 solution follows:"

# First I imported the hw1_test file then I printed the individual values of the letters
import hw1_test

print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f



print "Problem 3 solution follows:"
# I imported hw1_test again and wrote it out.
import hw1_test
print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))


### Travis Goodroad
### Ian Hooper
### Alejandro

# ... List your collaborators here, as a comment (on a line starting with "#").
