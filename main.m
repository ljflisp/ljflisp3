int main(){
ljflisp *pai=[[ljflisp alloc]init];
for(int i= 0;i<150000;i++){
[pai iterate];
}
double result= [pai getli];

NSLog(@"\npi= %.15f \n ",result);
return 0;
}