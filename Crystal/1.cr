puts "Enter number N:"
N=read_line.to_i
if N<0
   raise "It must be nonnegative"
end
while index<=N
  alternate= (-1)**(index-1)
 # sum= sum+(1/index)*alternate
  #index= index+1
end
puts "Sum: #{sum}"