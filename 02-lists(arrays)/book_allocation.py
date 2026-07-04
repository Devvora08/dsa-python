# // Given an array of integers A of size N and an integer B.
# // College library has N bags,the ith book has A[i] number of pages.
# // You have to allocate books to B number of students so that maximum number of pages alloted to a student is minimum

# // Input 1:
# //     A = [12, 34, 67, 90]
# //     B = 2
# // Output 1:
# //     113
# // Explanation 1:
# //     There are 2 number of students. Books can be distributed in following fashion : 
# //         1) [12] and [34, 67, 90]
# //         Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
# //         2) [12, 34] and [67, 90]
# //         Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
# //         3) [12, 34, 67] and [90]
# //         Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

# //         Of the 3 cases, Option 3 has the minimum pages = 113.

def isValid(pages, n,m, maxAllottedPages):
    students = 1
    page = 0

    for i in range(n):
        if pages[i] > maxAllottedPages:
            return False
        
        if page + pages[i] < maxAllottedPages:
            page = page + pages[i]
        else:
            students = students+1
            page = pages[i]

    if students > m:
        return False
    return True

def min_max_pages(pages, n, m):
    if m > n: # basic check if sudents greater than books
        return -1
    
    sum = 0
    for i in range(len(pages)):
        sum = sum + pages[i]
    
    # start = 0, end = sum
    end = sum
    start = 0
    ans = -1

    while start <= end:
        mid = start + (end-start)//2

        if isValid(pages, n,m, mid):
            ans = mid
            end = mid-1
        else:
            start = mid+1
    
    return ans


pages = [12,34,67,90]
n = len(pages)
m = 2

print(min_max_pages(pages, n, m))