#!/usr/bin/env python3

import random

def main():

    #part1
    wordbank= ["indentation", "spaces"]
    #part2
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    #part3
    wordbank.append(4)
    #part4/part5 make it an int instead of a string/bonus2 get the length of tlgstudents then minus 1 on the input to equal the index
    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    student_name = tlgstudents[num] #bonus1 = random.choice(tlgstudents)
    #part6
    print('{} always uses {} {} to indent.'.format(student_name, wordbank[2], wordbank[1]))

if __name__ == "__main__":
    main()

