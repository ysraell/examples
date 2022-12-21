/*42 is the answer!*/

#define THE_ANSWER 42

int i_am_global = THE_ANSWER;

int square(int x)
{
    return x * x;
}

int main(int argc, char** argv)
{
    return square(i_am_global);
}

/*EOF*/