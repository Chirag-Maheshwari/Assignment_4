class Point:
	def __init__(self):
		self.x= 0
		self.y= 0
		self.quad= 0
		self.dist= 0
		self.slope= 0.0

def print_point(p):
	print (str(p.x)+" "+str(p.y))


def get_slope(p1, p2):
	num = p2.y - p1.y
	den = p2.x - p1.x
	if(den!=0):
		return num/den
	else:
		if(num==0):
			return 0
		if(num<0):
			return -DBL_MAX
		return DBL_MAX
	
def cal_dis(p, q):
	return pow(p.x-q.x, 2) + pow(p.y-q.y, 2)


def swap(p, q):
	temp=p
	p=q
	q=temp

def cmp(p, q):
	if(p.quad != q.quad):
		return p.quad < q.quad
	if(p.slope == q.slope):
		return p.dist < q.dist
	return p.slope < q.slope


int orientation( p, q, r):
	val = (q.x-p.x)*(r.y-q.y)-(r.x-q.x)*(q.y-p.y)
	if(val>0):
		return 1
	if(val==0):
		return 0
	return -1


n= int(input("No of points"))
point= Point()
convex_hull_set= Point()
for i in range(0,n):
	print(point[i].x,point[i].y)

h=0
traversed= []
for i in range(0,n):
	traversed[i]=0;
	if(i!=0):
		if(point[i].y < point[0].y):
				swap(point[i], point[0])
		elif(point[i].y == point[0].y):
			if(point[i].x < point[0].x):
				swap(point[i], point[0])

point[0].slope = 0
point[0].quad = 1
point[0].dist = 0
for i in range(0,n):
	point[i].slope=get_slope(point[0], point[i])
	if(point[i].slope < 0):
		point[i].quad = 2
	else:
		point[i].quad = 1
	point[i].dist = cal_dis(point[i], point[0])

sort(point, point+n, cmp)


modified_list= []
m=1;
modified_list.append(point[0])
for i in range(0,n){
	if(point[i].slope != point[i+1].slope):
		modified_list[m++]=point[i]

modified_list[m++]=point[n-1]
convex_hull_set[0]=modified_list[0]
convex_hull_set[1]=modified_list[1]
h=2

for i in range(0,m):
	direction = orientation(convex_hull_set[h-2]
	if(direction == 1):
		convex_hull_set[h++]=modified_list[i]
	else:
		convex_hull_set[h-1]=modified_list[i]
		while (direction != 1):
			direction = orientation(convex_hull_set[h-3]
			if(direction !=1 ):
				convex_hull_set[h-2] = convex_hull_set [h-1]
				h-= 1
print (h)				
for i in range(0,n):
	print_point(convex_hull_set[i])