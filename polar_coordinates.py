#https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import phase
import re

cmplx_no = input()
pattern1 = re.compile(r'([-+]?\d+(?:\.\d+)?)|([-+]?\d+(?:\.\d+)?j)')
match1 = pattern1.findall(cmplx_no)
real_part = match1[0][0]
imag_part = match1[1][0]
print(abs(complex(float(real_part), float(imag_part))))
print(phase(complex(float(real_part), float(imag_part))))
