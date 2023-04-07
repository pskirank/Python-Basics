#Problem-1:
def average(array):
    # your code goes here
    print("Array Sum:", sum(array))
    print("Array Length:", len(set(array)))
    val = sum(set(array)) / len(set(array))
    return val

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#problem-2: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
m = input()
set1 = set(map(int, input().split()))
o = input()
set2 = set(map(int, input().split()))
for i in sorted(list(set1.difference(set2)) + list(set2.difference(set1))):
    print(i)


#Problem-3: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
arr_len, set_len = map(int, input().split())
h = 0
arr1 = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
for i in arr1:
    if i in set1:
        h += 1
    elif i in set2:
        h -= 1
print(h)

#Problem-4: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
N = int(input())
set1 = set()
for i in range(N):
    set1.add(input())
print(len(set1))

#problem-5: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    x = input().split()
    if x[0] == 'pop':
        s.pop()
    elif x[0] == 'discard':
        s.discard(int(x[1]))
    elif x[0] == 'remove':
        s.remove(int(x[1]))
print(sum(s))

#Problem-6: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))
print(len(set_english.union(set_french)))

#Problem-7: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
set_english = set(map(int, input().split()))
b = int(input())
set_french = set(map(int, input().split()))
print(len(set_english.intersection(set_french)))

#Problem-8: https://www.hackerrank.com/challenges/py-set-difference-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
set1 = set(map(int, input().split()))
b = int(input())
set2 = set(map(int, input().split()))
print(len(set1-set2))

#problem-9: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
n = int(input())
set1 = set(map(int,input().split()))
b = int(input())
set2 = set(map(int,input().split()))
print(len(set1^set2))

#problem-10:https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
seta_cnt = int(input())
A = set(map(int,input().split()))
other_sets_cnt = int(input())
for i in range(other_sets_cnt):
    input2 = input().split()
    set2 = set(map(int, input().split()))
    if input2[0] == 'intersection_update':
        A.intersection_update(set2)
    elif input2[0] == 'update':
        A.update(set2)
    elif input2[0] == 'symmetric_difference_update':
        A.symmetric_difference_update(set2)
    elif input2[0] == 'difference_update':
        A.difference_update(set2)
print(sum(A))
