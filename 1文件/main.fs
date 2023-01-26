let mutable p= 3.0
let mutable s= 2.0
let mutable a= 1.0

let iterate() = 
 p <- p+s*(4.0/(a*(a*(a+3.0)+2.0)))
 a <- a+2.0
 s <- -s
for _ in [0..150000] do
 iterate()
 
System.Console.Write("pi= ")
System.Console.Write(p)