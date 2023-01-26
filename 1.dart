//print("helloworld")
class Ljflisp {
  double p = 3.0;
  double a= 2.0;
  double s=  1.0;

  Ljflisp();
  
   void iterate() {
     p += s*(4/(a*(a*(a+3)+2)));
     a += 2;
     s = -s;
   }
}
void main(List<String> args){
  Ljflisp pi= new Ljflisp();
  for( int i=0;i<150000;i++){
    pi.iterate();
  }
  print("pi= " + pi.p.toString());
}