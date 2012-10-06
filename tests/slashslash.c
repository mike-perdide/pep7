#include <stdio.h>

int main() // this is the main function
{
    // printing hello world
    printf("Hello world\n"); // this line prints "Hello world"
    return 0;

    /*
     *  // this shouldn't be detected
     */
}
/*
 * TESTS RESULTS:
 * 3:12: E601 Never use C++ style // one-line comments
 * 5:5: E601 Never use C++ style // one-line comments
 * 6:30: E601 Never use C++ style // one-line comments
 */
