#https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def wrapper(f):
    def fun(l):
        # complete the function
        list1 = []
        for i in l:
            i=i[-10:]
            list1.append(i)
        list1 = sorted(list1)
        for j in list1:
            print('+91',j[-10:-5],j[-5:])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
