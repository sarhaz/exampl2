
class Solution:
    def is_palindrome(self, x: int):
        if x < 0:
            print("minus number")
            return False

        else:
            print("plus number")
            return True


x = int(input("Enter number: "))
sol = Solution()
print(sol.is_palindrome(x))