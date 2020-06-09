---
layout: post
title: "Python 3: Sliding Window Iteration"
date: 2020-06-08 12:00:00 -0000
categories: PYTHON 
---
### The Sliding Window Iterator

The sliding window iterator is an effective method of iterating through a list to evaluate sequential values. 

One leetcode challenge is to look through a string and identify the longest substring that doesn't have a repeating character. 

For example, in the following string:
    
    example_string = 'abbbcabc'

The solution substring we are looking for would be:

    longest_substring = 'abc'

An implementation of the sliding method is as follows, leveraging a dicussion submission from user 'clfm' on leetcode:


{% highlight python %}
s = 'abbbcabc'

longest, left, right = 0, 0, 0

hash_set = set() 

while right < len(s):
    #remember that the starting value of right is 0 so this starts index s[0]
    #the sliding window evaluates the rightmost character against the hashset
    if s[right] not in hash_set:

        #if the character doesn't exist in the hash set, add it
        hash_set.add(s[right])
        #increment the index after adding the character
        right += 1 
        #we're looking for the longest length as an integer. right-left calculates the string length
        longest = max(longest, right - left)
    else:
        #if the character does exist, we remove the leftmost character in our hashset 
        hash_set.remove(s[left])
        #then slide the window by incrementing the left index value
        left += 1

print(longest)

{% endhighlight %}