#!/usr/bin/python3.6
import os
import sys
homedir = os.getcwd()
class _Book():
    def Chapter1():
        def Sequence():
            print("Chapter 1. Data Structures")
            p = (4, 5)
            x, y = p
            print("#C1.1.1 x=", x)
            print("#C1.1.2 y=", y)

            data = ['Acme', 50, 91.1, (2012, 12, 21)]
            name, shares, price, (year, mon, day) = data
            print("#C1.1.3 Year, mon, day ", year, mon, day)

            _, shares, price, _ = data
            print("#C1.1.4 _, shares, prince, _", shares, price)
        def Arbitrary_Length():
            record = ('Dave', 'dave@acme.com', '777-777-7777', '555-555-5555')
            name, email, *phone_numbers = record
            print("#C1.2.1 name, email, *phone_numbers", phone_numbers)

            records = [
                ('foo', 1, 2),
                ('bar', 'hello'),
                ('foo', 3, 4)
                ]
            def do_foo(x, y):
                print('#C1.2.2 - foo', x, y)

            def do_bar(s):
                print('#C1.2.3 - bar', s)

            for tag, *args in records:
                if tag == 'foo':
                    do_foo(*args)
                elif tag == 'bar':
                    do_bar(*args)

            line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
            uname, *fields, homedir, sh = line.split(':')
            print("#C1.2.4 - fields ", fields)

        #Sequence() #Page 19/706
        Arbitrary_Length()
_Book.Chapter1()

