#Example
#class String
 # ALPHABET = ("A".."Z").to_a

 # def caesar_cipher(num)
    #self.tr(ALPHABET.join, ALPHABET.rotate(num).join)
  #end
#end

#encrypted = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG".caesar_cipher(5)
#decrypted = encrypted.caesar_cipher(-5)
#puts encrypted

class String 
  ALPHABET = ("A".."Z").to_a

  def caesar_cipher(num)
    self.tr(ALPHABET.join,ALPHABET.rotate(num).join)
  end
end

encrypted="DAD HAPPY BIRTHDAY!".caesar_cipher(2)
decrypted=encrypted.caesar_cipher(-2)
#puts encrypted
#puts decrypted

#def quick_sort(a : Array(Int32)) : Array(Int32)
 # return a if a.size <= 1
#  p = a[0]
 # lt, rt = a[1 .. -1].partition { |x| x < p }
 # return quick_sort(lt) + [p] + quick_sort(rt)
#end

#a = [7, 6, 5, 9, 8, 4, 3, 1, 2, 0]
#puts quick_sort(a) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def quick_sort(a : Array(Int32)) :   Array(Int32)
   return a if a.size<= 1
   p = a[0]
   lt , rt = a[1..-1].partition{ |x| x < p}
   return quick_sort(lt) + [p] + quick_sort(rt)
end
a=[7,6,5,9,8,4,3,1,2,0]
#puts quick_sort(a)
