# Common Bit Operations

* x%2==1 -> (x&1)==1
* x%2==0 -> (x&1)==0
* x>>1 -> x=x/2
* clear the lowest one
  * x=x&(x-1)
* get the lowest one
  * p=x&-x
* x*~x=0
