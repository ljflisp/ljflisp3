class Main{
  static public function main():Void{
    var pai= new Ljflisp();
    
    for(i in 0...150000){
      pai.iterate();
    }
    var pi= pai.getpi();
    
    #if sys
      Sys.println("pi= " + pi);
    #else
      trace("pi= " + pi);
    #end
  }
}