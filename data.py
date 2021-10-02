import sqlite3

con = sqlite3.connect("dogs.db")
cur = con.cursor()
last_id = 1

def norm(x):
	(ind,timer,a,b,c,d
		)=x[0],x[1],x[2],x[3],x[4],x[5]
	rd=list(x[6:])
	return {"ind":ind,"timer":timer,"h":[a,b,c,d],"rd":rd}

def sd(rodoslov_count):
	y=",".join([f"r{x} double(3)" for x in range(rodoslov_count)])
	cur.execute(f'''create table dogs (dogid INTEGER PRIMARY KEY AUTOINCREMENT,timer int,a double(3),b double(3),c double(3),d double(3),{y})''')

#{id:{rd:[],h:[]}}
def s(slov):
	h=slov["h"]
	x=tuple([13,h[0],h[1],h[2],h[3]]+slov["rd"])
	b=len(list(cur.execute("pragma table_info(dogs)")))-6
	y=",".join([f"r{x}" for x in range(b)])
	cur.execute(f'insert into dogs (timer,a,b,c,d,{y}) values {str(x)}')

def vv():
	return list(map(norm,cur.execute("select * from dogs")))

def u(ind):
	cur.execute(f"delete from dogs where dogid={ind}")

def ut():
	cur.execute("update dogs set  timer = timer-1")
	cur.execute("delete from dogs where timer=0")

def vs():
	n=norm(cur.execute(f'select * from dogs where dogid={last_id}'))
	last_id=last_id+1
	return n

def oo():
	last_id=1

def z():
	con.commit()

def vn(ind):
	return norm(list(cur.execute(f"select * from dogs where dogid={ind+1}"))[0])

def vz():
	global cur,con
	cur.close()
	con.close()
	con = sqlite3.connect("sobaki.db")
	cur = con.cursor()