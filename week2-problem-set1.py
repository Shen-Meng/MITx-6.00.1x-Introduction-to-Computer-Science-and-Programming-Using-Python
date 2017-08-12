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
longest_sub_list = [s[0]]
longest_sub = s[0]
for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        longest_sub += s[i+1]
        longest_sub_list.append(longest_sub)
    else:
        longest_sub = s[i+1]
max = 0
for i in range(1,len(longest_sub_list)):
    if len(longest_sub_list[max]) >= len(longest_sub_list[i]):
        pass
    else:
        max = i
print 'Longest substring in alphabetical order is: ' +  longest_sub_list[max]