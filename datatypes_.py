#data types
'''
Number(int,float,complex)
string(str)
tuple
list
dictinary(dict)
set
'''
# boolean types(bool)
'''
True
False
'''
#NUMBER
a=5
b=5.0
c=2+4j
print(type(a))
print(type(b)) 
print(type(c))
#string
a="hello world"
b='''hello
    world'''
c='hello world'
 #012345678910

print(type(a))
print(b)
print(c)
print(a.upper())
print(a.isupper())
print(a.islower())
print(a.title())
print(a.capitalize())
print(a.index("d"))
print(a[10])
print(a[0:5])
print(a[-2])  
print(a.index("w"))
print(a.replace("world","hema"))
print(a .lstrip())
print(a.strip(' '))
print("{} string data ".format(a))
print("string data{} ".format(a))
print(dir(a))  
x={"x":4,"y":10}
print("{x} hello {y}".format_map(x))

m={"x":4,"y":10,"z":20}
print("{x} hello {y}".format_map(m))
print("{x} new ".format_map(m))
print("{x} hello {y}".format(**m))
print("{x} hello,world {y}".format(**m))
print("{x} middle {y}".format(**m))
print("{x} middle".format(**m))
print("hello,world {y}".format(**m

print("{x} hello".format_map(m))
print("{y} new".format_map(m))
print("{z} world".format_map(m))