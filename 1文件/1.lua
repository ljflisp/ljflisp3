function addto(x)
  return function(y)
    return x + y
  end
end

fourplus = addto(4)
--print(fourplus(3))
function factorial(n)
  if n ==  0 then
    return 1
  else
    return n * factorial(n-1)
  end
end
--return factorial(100)
--print(factorial(100))

for i= 1, 5 do
  print("A number is :"..i)
end
point =  { x = 10, y = 20}
print(point["x"])
print(point.x)