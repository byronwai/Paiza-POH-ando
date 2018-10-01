str = input()
num_c = str.count('c')
num_a = str.count('a')
num_t = str.count('t')

minimum = min(num_c,num_a,num_t)
maximum = max(num_c,num_a,num_t)

print(minimum)

if num_c==maximum:
	print("0")
	print(maximum-num_a)
	print(maximum-num_t)
elif num_a==maximum:
	print(maximum-num_c)
	print("a")
	print(maximum-num_t)
elif num_t==maximum:
	print(maximum-num_c)
	print(maximum-num_a)
	print("0")