import math
def sum_of_squares(n):
    # put your code here...
    if int(math.sqrt(n)) ** 2 == n: # if n is a perfect square
        return 1
    min_num = float('inf')
    for i in range(1, int(math.sqrt(n))+1):
        j = int(math.sqrt(n - i*i))
        if i*i + j*j == n:
            min_num = min(min_num, 2)
        k = int(math.sqrt(n - i*i - j*j))
        if i*i + j*j + k*k == n:
            min_num = min(min_num, 3)
    if min_num == float('inf'):
        return 4
    return min_num
  
test.describe("Testing sum_of_squares: easy test cases")
test.assert_equals(sum_of_squares(15), 4)
test.assert_equals(sum_of_squares(16), 1)
test.assert_equals(sum_of_squares(17), 2)
test.assert_equals(sum_of_squares(18), 2)
test.assert_equals(sum_of_squares(19), 3)
