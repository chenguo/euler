#include <iostream>

using std::cout;
using std::endl;

int main ()
{
  int n1 = 1;
  int n2 = 2;
  int max = 4000000;
  int sum = 0;

  while (n2 <= max)
  {
    if ((n2 & 0b1) == 0)
    {
      sum += n2;
    }
    int tmp = n1;
    n1 = n2;
    n2 += tmp;
  }

  cout << "Total: " << sum << endl;
}
