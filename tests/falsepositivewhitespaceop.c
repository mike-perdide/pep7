#include <stdio.h>

int main()
{
    int foul;
    int bowl;

    foul=10;
    bowl=2;
    /* int bla=0; shouldn't raise errors
     */
    foul = 20;
    printf("Hello world\n"); /* bla=2; shouldn't raise errors
    */
    return 0;

    /*
     *  // C++ style comment that shouldn't be detected
     */


}

/*
 * TESTS RESULTS:
 * 8:9: E225 missing whitespace around operator
 * 9:9: E225 missing whitespace around operator
 */
