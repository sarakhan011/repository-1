class Solution:
    def rotate(self, number, rev):
        rev %= len(number)

        number.reverse()
        number[:rev] = reversed(number[:rev])
        number[rev:] = reversed(number[rev:])

list_of_nums = list(map(int,input("Enter a Number = ").split(",")))

rotation = int (input("Enter number of rotation = "))
sol = Solution()
sol.rotate (list_of_nums,rotation)
print ("reversed list is = ", list_of_nums)
