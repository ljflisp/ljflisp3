#print("helloworld")
#print("I love R.")
p<-3
a<-2
s<-1

iterate-> function() {
  p<<- p+s*(4/(a*(a*(a+3)+2)))
  a<<- a+2
  s<<- -s
}

i<-0
while(i<150000){
  iterate()
  i<<-i+1
}
print( paste("pi= ",p))