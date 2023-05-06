#https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for i in attrs:
            print('->', i[0], '>', i[1])

parser = MyHTMLParser()
N = int(input("Enter the number of Lines:"))
for i in range(N):
    parser.feed(input("Enter the script lines:"))
