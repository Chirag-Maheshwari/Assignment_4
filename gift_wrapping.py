class Point:
	def __init__(self):
		self.x= 0
		self.y= 0

def print_point(p):
	print (str(p.x)+" "+str(p.y))

int orientation(a, b, c):
	temp = a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y)
	if(temp>0):
		return 1
	if(temp<0):
		return -1
	return 0

print("No. of points= ")
n= int(input())
point= Point()
print("Enter the description of "<<n<<" points:\n")
for i in range(0,n):
	point.x= int(input("enter x of point"))
	point.y= int(input("enter y of point"))

convex_hull= []
h=0

l= 0
for i in range(1,n):
	if(point[i].x < point[l].x):
		l=i
	

p=1
while(p!=l):
	convex_hull_set[h++]=point[p];
	q=(p+1)%n;
	for i in range(0,n):
		if(orientation(point[p], point[i], point[q]) == -1):
			q=i
	p=q
print("Convex hull set points:\n")
print("h="<<h<<endl)
for i in range(0,h):
	print_point(convex_hull_set[i]);