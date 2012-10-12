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
    """Never use C++ style // one-line comments.

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
next_line_is_bracket = False
bracket_level = 0
open_function = False
open_local_variables = False


def function_def_style(physical_line):
    """Function definition style.

    Function name in column 1, outermost curly braces in column 1.

    Okay: int something()\n{\n ... \n}\n
    E723: int something() {\n ... \n}\n
    E723: int something(){\n ... \n}\n
    E723: int something()\n{\n ... code;}\n
    E723: int something()\n\n{\n ... code;}\n
    """
    global next_line_is_bracket
    global open_function
    global bracket_level

    error = "E723 Check function def style"

    function_regex = re.compile("\w+\s+.*\(.*\)\s*({?)$")

    if function_regex.search(physical_line):
        # This is a function definition line
        open_function = True

        if '{' in physical_line:
            # The opening bracket is on the same line as the function
            # declaration.
            idx = physical_line.index("{")
            bracket_level += 1

            return idx, error + " ('{' on function declaration line)"
        else:
            next_line_is_bracket = True

    elif next_line_is_bracket:
        # This has been set in a previous execution, it means this line
        # includes an opening bracket.
        if "{" not in physical_line:
            # This means the opening bracket doesn't follow the function
            # declaration line.
            return 0, error + " (blank line before '{')"

        next_line_is_bracket = False
        bracket_level += 1

        idx = physical_line.index("{")
        if idx != 0:
            return idx, error + " ('{' not in col 1)"

    elif open_function:
        # This is neither a function declaration line nor an "opening bracket"
        # line. We will count the number brackets and detect the closing
        # bracket for the current function.
        bracket_level += physical_line.count("{")
        bracket_level -= physical_line.count("}")

        if bracket_level == 0:
            # This means this line contains the closing bracket for the current
            # function.
            open_function = False

            idx = physical_line.index("}")
            if idx != 0:
                return idx, error + " ('}' not in col 1)"


def blank_line_local_vars(physical_line):
    """Blank line after local variable declarations.

    Okay: int something()\n{\n ... \n}\n
    E723: int something() {\n ... \n}\n
    E723: int something(){\n ... \n}\n
    E723: int something()\n{\n ... code;}\n
    E723: int something()\n\n{\n ... code;}\n
    """
    global open_local_variables
    global blank_line_after_local_var

    error = "E723 Missing blank line after local variable declarations"

    var_declaration_regex = re.compile("[a-zA-Z_-] [&*a-zA-Z_-]+ (= .*)+;$")
    blank_line_regex = re.compile("^\s*$")

    if var_declaration_regex.search(physical_line):
        open_local_variables = True

    else:
        # This isn't a variable declaration line
        if blank_line_regex.search(physical_line):
            open_local_variables = False

        elif open_local_variables:
            # This is not a blank line nor a variable declaration
            open_local_variables = False

            return 0, error


pep8.function_def_style = function_def_style
pep8.blank_line_local_vars = blank_line_local_vars

# Code structure:
# - one space between keywords like if, for and the following left paren;
# - no spaces inside the paren;
# - braces may be omitted where C permits but when present, they should be
# formatted as shown:
#
#       if (mro != NULL) {
#       ...
#       }


def return_statement_redundant_paren(logical_line):
    """The return statement should not get redundant parentheses

    Okay: return value;
    E722: return(value);
    """
    error = "E722 The return statement should not get redundant parentheses"

    return_paren = re.compile(r'return\s*(\(.*|.*\);)')

    if return_paren.search(logical_line):
        idx = logical_line.index("(") or logical_line.index(")")
        yield idx, error

pep8.return_statement_redundant_paren = return_statement_redundant_paren


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


### Heavy hacking begins

# Adding a filtering method between tokenize and pep8.
in_multiline_comment = False


def filter_generate_tokens(self):
    """Filter the tokens generated by tokenize.

    This acts by :
        - filtering out /* ... */ comments
        - fixing the type of tokens for emptied logical lines
        - fixing the type of tokens for end of C lines (";\n")
    """
    global in_multiline_comment

    previous_token = None
    skip_slash = False

    tokens_on_this_line = 0

    for token in legit_generate_tokens(self):
        if skip_slash:
            # This is the "/" corresponding to the second character in "*/".
            # Therefore, it should be skipped.
            assert previous_token[1] == "/"
            skip_slash = False
            previous_token = token
            continue

        if previous_token:
            if previous_token[1] == '/' and token[1] == '*':
                in_multiline_comment = True

            elif in_multiline_comment and \
                    previous_token[1] == '*' and token[1] == '/':

                in_multiline_comment = False
                skip_slash = True

            elif not in_multiline_comment:
                if previous_token[1] == ";" and token[1] == "\n":
                    # This is the end of a logical line, not detected by
                    # tokenize
                    token = (4,) + token[1:]

                elif previous_token[0] == 4 and tokens_on_this_line == 0:
                    # If we don't have any token on this line (because they've
                    # been filtered out), don't yield a logical line end token.
                    previous_token = (54,) + previous_token[1:]

                if previous_token[0] == 54 or previous_token[0] == 4:
                    tokens_on_this_line = 0
                else:
                    tokens_on_this_line += 1

                yield previous_token

        previous_token = token

    yield previous_token


legit_generate_tokens = pep8.Checker.generate_tokens
pep8.Checker.generate_tokens = filter_generate_tokens


# Finally launching pep8
pep8._main()
