#include <iostream>
#include <stdlib.h>

using namespace std;

// Get sum of multiples of n <= total
int get_sum (int n, int total)
{
  int num = total / n;
  int mult = (1 + num) * num / 2;

  return mult * n;
}

// Brute force get sum
int brute_get_sum (int n1, int n2, int total)
{
  int sum = 0;
  for (int i = 0; i < total; i++)
  {
    if ((i % n1) == 0 || (i % n2) == 0)
      sum += i;
  }
  return sum;
}

int main (int argc, char *argv[])
{
  if (argc != 4)
  {
    cerr << "Need 3 arguments received " << argc << endl;
  }

  int n1 = atoi(argv[1]);
  int n2 = atoi(argv[2]);
  int total = atoi(argv[3]);

  int sum_n1 = get_sum (n1, total - 1);
  int sum_n2 = get_sum (n2, total - 1);
  int overlap = get_sum (n1 * n2, total - 1);

  int answer = sum_n1 + sum_n2 - overlap;
  cout << "Sum 1: " << sum_n1 << " Sum 2: " << sum_n2 << " Overlap: " << overlap << " Answer: " << answer << endl;
  cout << "Brute force answer: " << brute_get_sum (n1, n2, total) << endl;
}
