@implementation ljflisp

- (id)init {
  self = [super init];
  if (self) {
  a= 2L;
  s= 1L;
  pi= 3L;
  }
  return self;
}
- (void)iterate {
 pi+= s*(4L/(a*(a*(a+3L)+2L)));
 a+= 2L;
 s= -s;
}
- (double)getpi {
return pi;
}
@end