/*

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

*/

list = [2]
int lastNum = 10001
int num = 3

def is_prime(int num){
  int counter = 2 //first prime number
  while (counter < num){
    if ((num % counter) == 0){
      return false
    }
    counter += 1
  }
  list.add(num)
  return true
}

while (list.size() < lastNum){
  is_prime(num)
  num += 1
}

println ('What is the 10001st prime number?')
println (list.last())
