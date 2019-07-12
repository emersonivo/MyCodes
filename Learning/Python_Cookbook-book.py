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
        
        def Keep_N():
            print("#C1.3 - Page 23/706")
            from collections import deque
            def search(lines, pattern, history=5):
                previous_lines = deque(maxlen=history)
                for line in lines:
                    if pattern in line:
                        yield line, previous_lines
                    previous_lines.append(line)
                # print(previous_lines)
                # previous_lines.appendleft("appendleft")
                # print(previous_lines)
                # previous_lines.append("appendright")
                # print('*'*20)

            if __name__ == '__main__':
                with open('somefile.txt') as f:
                    for line, prevlines in search(f, 'python', 5):
                        for pline in prevlines:
                            print(pline, end='')
                        print(line, end='')
                        print('-'*20)

        def find_Largest_Smallest():
            print("#C1.4 - Page 25/706")
            import heapq
            portfolio = [
                {'name': 'IBM', 'shares': 100, 'price': 91.1},
                {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                {'name': 'FB', 'shares': 200, 'price': 21.09},
                {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                {'name': 'YHOO', 'shares': 45, 'price': 16.35},
                {'name': 'ACME', 'shares': 75, 'price': 115.65}
                ]
            cheap = heapq.nsmallest(2, portfolio, key=lambda s: s['price'])
            expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
            print(cheap)
            print(expensive)
        
        def Remove_Duplicates():
            def dedupe(items):
                seen = set()
                for item in items:
                    if item not in seen:
                        yield item
                        seen.add(item)

            a = [1, 2, 5, 1, 9, 1, 5, 10]
            print("#C1.10.1 ", list(dedupe(a)))

        #Sequence() #Page 19/706
        #Arbitrary_Length()
        #Keep_N()
        #find_Largest_Smallest()
        Remove_Duplicates()

_Book.Chapter1()


