#include <stdio.h>

int main(void)
{
    int a[] = {10, 20, 30, 40};
    for (int i = 0 ; i <4 ; i++)
    {
        printf("%d\n", a[i]);
    }

    int n = 0;
    for( n = 0; n < 20; n++ ) {
        if (n % 2) continue;
        printf("%d is odd\n", n );
    }

    int i = 10;
    switch ( i ) {
        case 1: /* if i is equal to 1...*/
            puts( "It is one\n" );
            break; /* Break is mandatory */
        case 2: /* if i is equal to 2...*/
            puts( "It is two\n" );
            break;
        default: /* otherwise... */
            puts( "It is not one nor two\n" );
            break;
    }


    return 0;
}

/*EOF*/