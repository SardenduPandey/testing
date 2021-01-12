def into_list(x):
	l = list(x)
	return l

def into_str(x):
	s = str(x)
	return s
def into_tuple(x):
	t = tuple(x)
	return t

x = input ("enter the data you want to convert into ::")
form = input(" enter the data type to convert::")
if form == 'str':
	print(into_str(x))
elif form == 'tuple' :
	print(into_tuple(x))