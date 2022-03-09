# if s[j] >= g[i] where s is size of cookie j and g is greed of child i
# want to maximize the number of 'content' children and output that maximum number
# example input g=[1,2,3], s = [1,1], output is 1
# you have 3 children and 2 cookies. The greed factors of 3 children are 1,2,3.
# You can only make the child whose greed factor is 1 content. Output is 1.
#ex. 2 - g = [1,2] s = [1,2,3], output is 2

def assigncookies(g, s):
	g = sorted(g)
	s = sorted(s)
	ans = 0
	i = 0
	j = 0
	while i<len(s) and j<len(g):
		if s[i]>=g[i]:
			ans+=1
			i+=1
			j+=1
		else:
			i+=1
	print(ans) 

g = [1,2] 
s = [1,2,3]
assigncookies(g,s)