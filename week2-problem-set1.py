#problem 1
count = 0
s = s.lower()
for char in s:
    if char in 'aeiou':
        count += 1
print "Number of vowels: %d" % count


#problem 2
count = 0
n = 0
for n in range(0,len(s)-2):
    sp = s[n:n+3]
    if sp == 'bob':
        count = count + 1
    n = n + 1
print 'Number of times bob occurs is: %d' % count


#problem 3
count = 0
n = 0
for n in range(0,len(s)-2):
    sp = s[n:n+3]
    if sp == 'bob':
        count = count + 1
    n = n + 1
print 'Number of times bob occurs is: %d' % count