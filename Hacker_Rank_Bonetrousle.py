#https://www.hackerrank.com/challenges/bonetrousle/problem

t = int(input("t="))
for _ in range(t):
    n, k, b = [int(x) for x in input("n,k,b values with spaces:").split()]
    cur_sum = int(b * (1 + b) / 2)
    res = [x + 1 for x in range(b)]
    if cur_sum > n:
        print(-1)
        continue
    max_shift = k - b;
    for i in reversed(range(b)):
        print(i)
        shift = min(max_shift, n - cur_sum)
        print(shift)
        res[i] += shift
        cur_sum += shift
    if cur_sum < n:
        print(-1)
        continue
    print(' '.join([str(x) for x in res]))
