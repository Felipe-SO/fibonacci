#returns selected term of the fibonacci sequence starting in 1, 1
def fibonum(term):
	count=0
	x=1
	y=0
	z=1
	while count < term-1:
		z=x
		x=x+y
		y=z
		count=count+1
	else:
		return x
    
#prints fibonacci sequence until up to the limit term
def fiboseq(limit):
    count=0
    x=1
    y=0
    z=1
    while count < limit-1:
        print(x)
        z=x
        x=x+y
        y=z
        count=count+1

#counts the digits of a certain term of the fibonacci sequence
def fibodigits(term):
    return(len(str(fibonum(term))))

#prints index of fibonacci value lesser than x
def fibolim(x):
    y=1
    while fibonum(y) < x:
        y+=1
    print(y-1)
    return y-1

#prints prints the index and value of the last fibonacci number lesser than limit
def fiboless(limit):
    print(fibonum(fibolim(limit)))
    

