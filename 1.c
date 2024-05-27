#include <stdio.h>
#include <cs50.h>
#include <string.h>
int binary_search(int a[], int number, int left, int right);
int main(int argc, string argv[])
{

    int number = get_int("Number \n");
    int numbers[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,21};

   int index = binary_search(numbers, number, 0 , 19);

   if (index == -1 )
   {
    printf("number %i is not on the list \n",number);
   }
   else
   {
     printf("index of %i is %i \n",number, index);

    return 0;
   }


}

int  binary_search(int a[], int number, int left, int right)
   {

    if(left > right)
    {
       return -1;
    }

    int mid = left + (right - left) /2;

    if(a[mid] == number)
    {
        return mid;
    }
    else if (a[mid] > number)
    {
      return binary_search(a, number, left, mid - 1);
    }
    else if (a[mid] < number)
    {
        return binary_search(a, number, mid + 1, right);
    }

    return 1;

   }