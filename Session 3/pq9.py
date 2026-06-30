'''
Take a student's marks as input. Print their grade based on this scale:
90 and above → A
75 to 89 → B
60 to 74 → C
40 to 59 → D
Below 40 → F
Q10: Take a year as in
'''

marks = int(input('Enter marks : '))

if marks >= 91 and marks <= 100:
    print('A')
elif marks >= 81 and marks <= 90:
    print('B')
elif marks >= 71 and marks <= 80:
    print('C')
elif marks >= 61 and marks <= 70:
    print('D')
elif marks >= 0 and marks <= 60:
    print('Fail')
else:
    print("Invalid Marks")
