#include <stdio.h>

int main()
{
    printf("Hello world\n");
    return 0;
}
int pain()
{
    printf("Hello world\n");
    return(0);
}
int vain()
{
    printf("Hello world\n");
    return (0);
}
/*
 * TESTS RESULTS:
 * 11:11: E722 The return statement should not get redundant parentheses
 * 16:12: E722 The return statement should not get redundant parentheses
 */
