#https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

cube = lambda x: x ** 3

def fibonacci(n):
    list1 = []
    x,y = 0,1
    for i in range(n):
        list1.append(x)
        x,y = y, x+y
    return(list1)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
