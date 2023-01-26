#puts "hello world"
array= [3,4,5]
value= 4
def linear_search(array,value)
    array.each do |element|
    if element== value
      return value
      puts "@value"
    elsif element>value
        break
    end
  end   
  return nil
end
say="I love Gabby!"
#10.times{puts say}
#puts "Do you like programming?"
#puts.getstrip()
str= "I will drill for a well in Hull."
regex= Regexp.new(/\w+ll/)
matchdata= regex.match(str)
while matchdata !=  nil
#  puts matchdata[0]
  str= matchdata.post_match
  matchdata=regex.match(str)
end  

#π
$pi= 3
$a= 2
$s= 1
def iterate()
  $pi += $s*(4.0/($a*($a*($a+3.0)+2.0)))
  $a += 2.0
  $s = -$s
end

150000.times do 
  iterate()
end

puts"pi= #$pi"