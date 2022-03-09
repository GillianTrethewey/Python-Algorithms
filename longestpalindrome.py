s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

def longestpalindrome(s):
	p = s[0]
	l = 1

	for i in range(len(s)): # 5
		for j in range(len(s),0,-1): # 5,0,-1 start, stop, increment
			w = s[i:j] 

			if w == w[::-1] and len(w) > 1: #w[::-1] REVERSES the string
				p = w
				l = len(w)

	print("The longest palindrome is ", p) 

longestpalindrome(s)

# w = str[i:j] ... 
# 1:5, 1:4, 1:3, 1:2, 1:1, 1:0 slice from 1 to 4, then 1 to 3
# 2:5, 2:4, 2:3, 2:2, 2:1, 2:0