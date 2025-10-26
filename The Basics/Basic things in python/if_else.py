# Given marks of a student, print on the screen:

# Grade A if marks >= 90
# Grade B if marks >= 70
# Grade C if marks >= 50
# Grade D if marks >= 35
# Fail, otherwise.


# For printing use:-

# for C++ : cout << variable_name;
# for Java : System.out.print();
# for Python : print()
# for Javascript : console.log()
# for C# : Console.WriteLine();
# for Go : fmt.Println()

# Examples:
# Input: marks = 95

# Output: Grade A

# Explanation: marks are greater than or equal to 90.

# Input: marks = 14

# Output: Fail

# Explanation: marks are less than 35.

class Solution:
    def studentGrade(self, marks):
        if marks >= 90:
            print("Grade A")
        elif marks>=70 and marks<90:
            print("Grade B")
        elif marks>=50 and marks<70:
            print("Grade C")
        elif marks>=35 and marks<50:
            print("Grade D")
        else:
            print("Fail")

if __name__ == "__main__":
    marks = int(input("Enter the marks:"))
    obj = Solution()
    obj.studentGrade(marks)