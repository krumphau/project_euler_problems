/*
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
*/

def list = []

def create_natural_numbers (int num_numbers, list){
  for (i in 1..num_numbers){
    list.add(i)
  }
  return list
}

def sum_of_squares(list){
  int sum_of_squares = 0
  for (l in list){
    sum_of_squares += (l*l)
  }
  return sum_of_squares
}

def square_of_sum( list ){
  int sum = 0
  for (l in list){
    sum += l
  }
  return sum*sum
}

create_natural_numbers( 100, list )
sum_of_squares = sum_of_squares(list)
square_of_sum = square_of_sum( list )

println ("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum:")
println (Math.abs(square_of_sum - sum_of_squares))
