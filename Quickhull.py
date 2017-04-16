# Quickhull algo for finding the convex hull points


class Point:
	def __init__(self):
		self.x= 0
		self.y= 0

def print_point(p):
	print (str(p.x)+" "+str(p.y))

# returns 2*area enclosed between three points: p, q and r
# or basically the absolute value of cross product of vectors p-q and q-r
def area(p,q,r):
	return abs(p.x*(q.y-r.y) + q.x*(r.y-p.y) + r.x*(p.y-q.y))

# actually this will calculate the square of the distance
# of a point r from the line formed by joining points p and q
def cal_dis(p,q,r):
	num= area(p,q,r)
	return num

Point *convex_hull_set;
int h=0;

convex_hull_set= Point()
h= 0


def get_sign(A, B, X):
	sign = (A.y-B.y)*X.x + (B.x-A.x)*X.y + (B.y*A.x-A.y*B.x);
	if(sign>0):
		return 1;
	if(sign<0):
		return -1;
	return 0;


def FindHull(point, n, A, B){
	if(n<=0):
		return;
	index=0
	max_dis= None
	temp_dis= None
	for i in range(0,n):
		temp_dis = cal_dis(A, B, point[i])
		if(i==0):
			max_dis=temp_dis
		elif(temp_dis > max_dis):
			max_dis = temp_dis
			index = i
	
	h+= 1
	convex_hull_set[h]=point[index]
	C= Point()
	C.x= point[index].x
	C.y= point[index].y
	G= Point()
	G.x = (A.x + B.x + C.x)/3;
	G.y = (A.y + B.y + C.y)/3;
	sign = get_sign(A, C, G);
	point_pos= Point()
	point_neg= Point()
	p=0
	q=0
	for i in range(0,n):
		if(sign*get_sign(A,C,point[i]) < 0):
			point_pos[p++]=point[i];
	
	sign = get_sign(B, C, G)
	for i in range(0,n):
		if(sign*get_sign(B,C,point[i]) < 0):
			point_neg[q++]=point[i]
	
	FindHull(point_pos, p, A, C);
	FindHull(point_neg, q, C, B);	



n= None
n= int(input("Number of points"))
Point *point = new Point[n];
point_a= Point()
convex_hull_set = new Point[n];
convex_hull_set= []
leftmost=0
rightmost=0;
for i in range(0,n):
	point[i].x= int(input("x of the point"))
	point[i].y= int(input("y of the point"))
	if(point[i].x < point[leftmost].x):
		leftmost=i
	if(point[i].x > point[rightmost].x):
		rightmost=i


point_pos= Point()
point_pos= Point()
A= None
B= None
C= None
A = point[leftmost].y - point[rightmost].y
B = -point[leftmost].x + point[rightmost].x
C = point[rightmost].y*point[leftmost].x - point[leftmost].y*point[rightmost].x

p=0
q=0
val= None
for i in range(0,n):
	if(i!=leftmost && i!=rightmost):
		val = A*point[i].x + B*point[i].y + C
		if(val>0):
			point_pos[p++]=point[i]
		if(val<0):
			point_neg[q++]=point[i]

convex_hull_set[h++] = point[leftmost]
convex_hull_set[h++] = point[rightmost]
FindHull(point_pos, p, point[leftmost], point[rightmost])
FindHull(point_neg, q, point[leftmost], point[rightmost])
cout<<"Convex hull set points:\n";
cout<<"h="<<h<<endl;
for i in range(0,h)
	print_point(convex_hull_set[i])

