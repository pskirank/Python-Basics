s = input("Enter the Time in 12Hr format:")
if s[8:] == 'AM':
    if s[0:2] == '12':
        hrs = '00'
        print(hrs+s[2:8])
    else:
        hrs = str(s[0:2])
        print(hrs+s[2:8])
elif s[8:] == 'PM':
    if s[0:2] == '12':
        hrs = str(s[0:2])
        print(hrs+s[2:8])
    else:
        hrs = str(int(s[0:2])+12)
        print(hrs+s[2:8])
