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
  