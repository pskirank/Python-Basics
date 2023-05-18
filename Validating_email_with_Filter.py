#https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true

import re
from email.utils import parseaddr

def fun(s):
    # return True if s is a valid email, else return False
    regex1 = r'[a-zA-Z0-9\_\-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}'
    if re.fullmatch(regex1,s):
        return True
    else:
        return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
