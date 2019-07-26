#!/usr/bin/python3.6
import os
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

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
        
        def Remove_Duplicates(): #35/706
            def dedupe(items):
                seen = set()
                for item in items:
                    if item not in seen:
                        yield item
                        seen.add(item)

            a = [1, 2, 5, 1, 9, 1, 5, 10]
            print("#C1.10.1 ", a)
            print("#C1.10.2 ", list(dedupe(a)))

        def Sorting_ListOfDict(): #40/706
            rows = [
                    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
                    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
                    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
                    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
                    ]

            from operator import itemgetter
            rows_by_fname = sorted(rows, key=itemgetter('fname'))
            print("#C1.13.1 Undorted: ", rows)
            print("#C1.13.2 Sorted: ", rows_by_fname)

        def Group_by_Value():
            rows = [
                {'address': '5412 N CLARK', 'date': '07/01/2012'},
                {'address': '5148 N CLARK', 'date': '07/04/2012'},
                {'address': '5800 E 58TH', 'date': '07/02/2012'},
                {'address': '2122 N CLARK', 'date': '07/03/2012'},
                {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
                {'address': '1060 W ADDISON', 'date': '07/02/2012'},
                {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
                {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
                ]
            for i in rows:
                print("#C1.15.1 ", i)
            from operator import itemgetter
            from itertools import groupby
            # Sort by the desired field first
            rows.sort(key=itemgetter('date'))
            # Iterate in groups
            for date, items in groupby(rows, key=itemgetter('date')):
                print(date)
                for i in items:
                    print('#C1.15.2 ', i)
        
        def MyDictTest():
            rec = [
                {
                'res':{
                    'attriba': {'name':'attriba', 'status':'PROV'},
                    'attribb': {'name':'attribb', 'status':'PROV'}
                    },
                'req':{
                    'attribc': {'name':'attribc', 'status':'REQ'},
                    'attribd': {'name':'attribd', 'status':'PROV'}
                    }
                }
            ]
            for i in rec:
                print("#MD1: ", i)
                for k1, v1 in i.items():
                    print("MD2.1: ", k1)
                    print("MD2.2: ", v1)
                    if 'req' in k1:
                        for k2, v2 in v1.items():
                            if 'PROV' in v2.values():
                                print("MD3.1: Resource", k1, k2, v2)

        def Filtering_Sequence():
            mylist = [1, 4, -5, 10, -7, 2, 3 -1]
            print("#C1.16.1", [n for n in mylist if n > 0])
        
        def Extracting_Dict_Subset():
            prices = {
                'ACME': 45.23,
                'AAPL': 612.78,
                'IBM': 205.55,
                'HPQ': 37.20,
                'FB': 10.75
                }

            print("#C1.17.1:", {key:value for key, value in prices.items() if value > 200})
        def Get_Local_files():
            homedir = os.getcwd()
            files = os.listdir(homedir)
            print("#C1.18.1: ", [name for name in files if name.endswith('.py')])

        # Sequence() #Page 19/706
        # Arbitrary_Length()
        # Keep_N()
        # find_Largest_Smallest()
        # Remove_Duplicates()
        # Sorting_ListOfDict() #40/706
        # Group_by_Value()
        # MyDictTest()
        # Filtering_Sequence()
        # Extracting_Dict_Subset()
        # Get_Local_files()
    
    def Chapter2():
        def Splitting_String_Multi_Delimiters():
            import re
            line = 'asdf fjdk; gfed, poslded, fjek,asdf, foo, Dat45, Dat01, Dat99/88FEP'
            print("#C2.1.1", re.split(r'[;,\s]\s*', line))
        
        def Using_Wildcard():
            import re
            from fnmatch import fnmatch, fnmatchcase
            line = 'asdf fjdk; gfed, poslded, fjek,asdf, foo, Dat45, Dat01, Dat99/88FEP'
            print("#C2.3.1", [s for s in re.split(r'[;,\s/]\s*', line) if s.startswith('g') or s.endswith('k')])
            print("#C2.3.2", [s for s in re.split(r'[;,\s/]\s*', line) if fnmatch(s, '?????ed')])
            print("#C2.3.3", [s for s in re.split(r'[;,\s/]\s*', line) if fnmatch(s, '*[0-9]')])
            print("#C2.3.4", [s for s in re.split(r'[;,\s/]\s*', line) if fnmatch(s, '[0-9]*')])

        # Splitting_String_Multi_Delimiters()
        Using_Wildcard()
_Book.Chapter2()


