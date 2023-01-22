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
puts"What is your name?"
name=gets.chomp
puts"Hello,"+name+",nice to meet you."
class Author
  attr_accessor :first_name
  
  def initialize(first_name,last_name,year_born)
    @first_name=first_name
    @last_name= last_name
    @year_born= year_born
  end
  
  def get_full_name() 
    @first_name+" "+@last_name
  end
end
author=Author.new("Dougla","Adams",1952)
author.first_name="Doug"
fullName=author.get_full_name()
puts fullName