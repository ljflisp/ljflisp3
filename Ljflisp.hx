class Ljflisp{
  private var s : Int ;
  private var pi : Float;
  private var a : Int;

  public function new() {
    s= 1;
    a= 2;
    pi= 3;
  }

  public function iterate(): Void{
    pi+= s*(4/(a*(a*(a+3)+2)));
    a+= 2;
    s= -s;
  }

  public function getpi(): Float {
    return pi;
  }
}