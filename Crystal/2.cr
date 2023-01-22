#puts "hello，world"
class String
  ALPHABET = ("a".."z").to_a
  def casear_cipher(num)
    self.tr(ALPHABET.join,ALPHABET.rotate(num).join)
  end
end

encryted="EJGPLKPI".casear_cipher(2)
decrypted= encrypted.casear_cipher(-2)
puts decrpted