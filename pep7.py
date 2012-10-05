#!/usr/bin/env python
import pep8
import re

### C Dialect

# Use ANSI/ISO standard C (the 1989 version of the standard). This means
# (amongst many other things) that all declarations must be at the top of a
# block (not necessarily at the top of function).

# Don't use GCC extensions (e.g. don't write multi-line strings without
# trailing backslashes).

# All function declarations and definitions must use full prototypes (i.e.
# specify the types of all arguments).


# Never use C++ style // one-line comments.
def slashslash_full_line_comments(physical_line):
    """
        Never use C++ style // one-line comments.

        E601: // some comment
    """
    full_line_slashslash = re.compile(r'^\s *//')
    inline_slashslash = re.compile(r'^\s*[^*]*//')

    if full_line_slashslash.search(physical_line) or \
       inline_slashslash.search(physical_line):
        idx = physical_line.index("//")
        return idx, "E601 Never use C++ style // one-line comments"

pep8.slashslash_full_line_comments = slashslash_full_line_comments


# No compiler warnings with major compilers (gcc, VC++, a few others).


### Code lay-out

# The following are provided by pep8
# - Use 4-space indents and no tabs at all.
# - No line should be longer than 79 characters.
# - No line should end in whitespace.

# Function definition style: function name in column 1, outermost curly braces
# in column 1, blank line after local variable declarations.

# Code structure:
# - one space between keywords like if, for and the following left paren;
# - no spaces inside the paren;
# - braces may be omitted where C permits but when present, they should be
# formatted as shown:
#
#       if (mro != NULL) {
#       ...
#       }

# The return statement should not get redundant parentheses

# Function and macro call style: foo(a, b, c) -- no space before the open
# paren, no spaces inside the parens, no spaces before commas, one space after
# each comma.

# Always put spaces around assignment, Boolean and comparison operators. In
# expressions using a lot of operators, add spaces around the outermost
# (lowest-priority) operators.

# Breaking long lines: if you can, break after commas in the outermost argument
# list.

# When you break a long expression at a binary operator, the operator goes at
# the end of the previous line.

# Put blank lines around functions, structure definitions, and major sections
# inside functions.

# Comments go before the code they describe.

# All functions and global variables should be declared static unless they are
# to be part of a published interface

# For external functions and variables, we always have a declaration in an
# appropriate header file in the "Include" directory, which uses the
# PyAPI_FUNC() macro.


### Naming conventions

# Use a Py prefix for public functions; never for static functions. The Py_
# prefix is reserved for global service routines like Py_FatalError; specific
# groups of routines (e.g. specific object type APIs) use a longer prefix, e.g.
# PyString_ for string functions.

# Public functions and variables use MixedCase with underscores, like this:
# PyObject_GetAttr, Py_BuildValue, PyExc_TypeError.

# Occasionally an "internal" function has to be visible to the loader; we use
# the _Py prefix for this, e.g.: _PyObject_Dump.

# Macros should have a MixedCase prefix and then use upper case, for example:
# PyString_AS_STRING, Py_PRINT_RAW.


### Documentation strings

# Use the PyDoc_STR() or PyDoc_STRVAR() macro for docstrings to support
# building Python without docstrings (./configure --without-doc-strings).

# The first line of each fuction docstring should be a "signature line" that
# gives a brief synopsis of the arguments and return value.

# Always include a blank line between the signature line and the text of the
# description.

# If the return value for the function is always None (because there is no
# meaningful return value), do not include the indication of the return type.

# When writing multi-line docstrings, be sure to always use backslash
# continuations, as in the example above, or string literal concatenation.

# Finally launching pep8
pep8._main()
