Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #string
>>> x= "sahil"
>>> x.upper()
'SAHIL'
>>> x = "SAHIL"
>>> x.lower()
'sahil'
>>> x.capitalize()
'Sahil'
>>> x = "hello how are u"
>>> x.capitalize()
'Hello how are u'
>>> x.title()
'Hello How Are U'
>>> x = "Hello How Are U"
>>> x.swapcase()
'hELLO hOW aRE u'
>>> x
'Hello How Are U'
>>> x.count('e')
2
>>> x.count('z')
0
>>> x
'Hello How Are U'
>>> x.index('H')
0
>>> x.index("H",0)
0
>>> x.index("H",1)
6
>>> x.find("H")
0
>>> x.find("H",1)
6
>>> x.index("z")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x.index("z")
ValueError: substring not found
>>> x.find("z")
-1
>>> #here -1 denotes value not found
>>> x
'Hello How Are U'
>>> x.find("H")
0
>>> x.rfind("H")
6
>>> x = "Himashu"
>>> len(x)
7
>>> x
'Himashu'
>>> x.center(7)
'Himashu'
>>> x.center(8)
'Himashu '
>>> x.center(9)
' Himashu '
>>> x.center(10)
' Himashu  '
>>> x.center(50)
'                     Himashu                      '
>>> x.center(50,"*")
'*********************Himashu**********************'
>>> x.center(60,"-")
'--------------------------Himashu---------------------------'
>>> x= '                     Himashu                      '
>>> x
'                     Himashu                      '
>>> x.lstrip()
'Himashu                      '
>>> x.rstrip()
'                     Himashu'
>>> x.strip()
'Himashu'
>>> x = '*********************Himashu**********************'
>>> x
'*********************Himashu**********************'
>>> x.lstrip()
'*********************Himashu**********************'
>>> x.lstrip("*")
'Himashu**********************'
>>> x.rstrip("*")
'*********************Himashu'
>>> x.strip("*")
'Himashu'
>>> x = "Java Programming"
>>> x.replace("Java","Python")
'Python Programming'
>>> x
'Java Programming'
>>> x.zfill(10)
'Java Programming'
>>> x = "java"
>>> x.zfill(10)
'000000java'
>>> x = "sahil"
>>> x.zfill(20)
'000000000000000sahil'
>>> x
'sahil'
>>> x.startswith('s')
True
>>> x.startswith('x')
False
>>> x
'sahil'
>>> x.endswith('l')
True
>>> chr(99)
'c'
>>> #chr - >ASCII - CHARACTER
>>> chr(102)
'f'
>>> #character -> ASCII
>>> ord('A')
65
>>> ord('B')
66
>>> ord('C')
67
>>> ord('@')
64
>>> 
============= RESTART: /Users/brainmentors/Documents/if-else001.py =============
go outside
>>> 
============= RESTART: /Users/brainmentors/Documents/if-else001.py =============
go outside but dont forgot the umbrella
>>> #OPerators
>>> #arithmetic operators +,-,/,*,%,**,//
>>> #comparison operator
>>> 5  > 5
False
>>> 5 < 10
True
>>> 5 <= 5
True
>>> 5 >= 1
True
>>> 5 == 5
True
>>> 5 == 10
False
>>> 5 != 10
True
>>> 5!=5
False
>>> 