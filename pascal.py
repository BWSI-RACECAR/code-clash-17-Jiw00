"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #17 - Pascal's Triangle (pascal.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Blaise Pascal is a famous French Mathematician and Philosopher who 
created Pascal's Triangle. Pascal's Triangle is a triangular array composed of 
binomial coefficients that arises in probability theory, combinatorics, and algebra. (Wikipedia)

Prompt: Given the number of rows, return a 2D list of Pascal's Triangle

Test Cases:
Input: rows = 1 ; Output = [[1]]
Input: rows = 2 ; Output = [[1], [1, 1]]
Input: rows = 3 ; Output = [[1], [1, 1], [1, 2, 1]]

"""

class Solution:
    def pascalTri(self,rows):
        # type row: int
        # return type: list[list[int]]
        pascal_list = []
        for n in range(rows):
            pascal_list.append([1])
            if n != 0:
                for m in range(1, n):
                    pascal_list[n].append(pascal_list[n - 1][m - 1] + pascal_list[n - 1][m])
            if n != 0:
                pascal_list[n].append(1)
        return pascal_list

        

def main():
    num = int(input())

    tc1 = Solution()
    ans = tc1.pascalTri(num)
    print(ans)

if __name__ == "__main__":
    main()