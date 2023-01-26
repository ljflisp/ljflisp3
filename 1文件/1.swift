//π
class ljflisp {
  var pi : Double = 3.0
  var a  : Double = 2.0
  var s  : Double = 1.0
  
  func iterate() {
    pi += s*(4.0/(a*(a*(a+3.0)+2.0)))
    a += 2.0
    s = -s
  }
}
var pai=ljflisp()
//... 3个点也可以
for _ in 0..<150000 {
  pai.iterate()
}
print("pi= \(pai.pi)")