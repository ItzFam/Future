# I just wanted to make a calculator and a converter.

# First, these are the imported functions that I will be using.

from cmath import sqrt
from math import cbrt
from math import sin, cos, tan, asin, acos, atan
from math import pi

# We need to make a while loop to keep the program running

while True:
 
 print("Welcome to calculator pro max")

 print("--------------------------------------------------------------------------------------------------")

 print("""
          1. Calculator
          2. Converter
          3. Trignometric functions
          4. Other functions
          5. Exit
          """)
# Choosing the function they want to perform

 function = int(input("Choose the function you want to perform: "))

 print("--------------------------------------------------------------------------------------------------")

 if function == 1:
  options = """
            1. Addition
            2. Subtraction
            3. Multiplication
            4. Division
            5. Percentage
            6. Square root
            7. Cube root
            8. Exponent
            9. Exit
            """
  print(options)

# Showing the user what operation they want to perform

  operation = str(input("Choose the operation you want to perform: "))

  print("--------------------------------------------------------------------------------------------------")

# This is where we are going to perform the operations
  def input_number():
              num1 = float(input("Enter the first number: "))
              num2 = float(input("Enter the second number: "))
              return num1, num2
  # Instead of using the input function again and again, we will make an input function
      
  if operation == "1":
    num1,num2 = input_number()
    print("The sum of", num1, "and", num2, "is", num1 + num2)
  elif operation == "2":
        num1,num2 = input_number()
        print("The difference of", num1, "and", num2, "is", num1 - num2)
  elif operation == "3":
        num1,num2 = input_number()
        print("The product of", num1, "and", num2, "is", num1 * num2)
  elif operation == "4":
        num1,num2 = input_number()
        if num2 == 0:
              print("Cannot divide by zero")
        else: 
              print(num1 / num2)
  elif operation == "5":
        num = float(input("Enter the number: "))
        print("The required percentage is: ",num / 100, "%")
  elif operation == "6":
        num = float(input("Enter the number: "))
        print("The root of the number is ",sqrt(num))
  elif operation == "7":
        num = float(input("Enter the number: "))
        print("The cube root of the number is ",cbrt(num))      
  elif operation == "8":
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the Exponent: "))
        print("The required answer is: ", num1**num2)
  elif operation == "9":
        print("Thank you for using the calculator")
        break
  else:
        print("Invalid operation")
        retry = str(input("Do you want to try again? (y/n): "))
        if retry == "y":
              continue
        elif retry == "n":
              print("Thank you for using the calculator")
              break

        # We need to make sure that the user dosen't input anything besides the options that is provided.

        # There we go the calculatior is done

      
 elif function == 2:
       print("""
             1. Length
             2. Mass
             3. Time
             """)

       measurment = int(input("Choose the measurment you want to convert:"))

       def input_unit():
             unit = int(input("Choose the unit you want to convert: "))
             return unit
            
            

       if measurment == 1:
             print("1. meters, 2. kilometers, 3. centimeters")
             unit = input_unit()
             print(input_unit())

             if unit == 1:
                   print("1. kilometers", "2. centimeters")
                   unit2 = int(input("Which unit you want to convert meters to: "))
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num / 1000)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num * 100)
                   else:
                         print("Invalid input")
             elif unit == 2:
                   print("1. meters", "2. centimeters")
                   unit2 = int(input("Which unit you want to convert kilometers to: ")) 
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num * 1000)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num * 10000)
                   else:
                         print("Invalid input")

             elif unit == 3:
                   print("1. meters", "2. kilometers")
                   unit2 = int(input("Which unit you want to convert centimeters to: "))
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num / 100)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num / 10000)
                   else:
                         print("Invalid input")
       elif measurment == 2:
             print("1. kilograms, 2. grams")
             unit = int(input("Choose the unit you want to convert: "))
             if unit == 1:
                   unit2 = int(input("Enter the values (to convert kg to g): "))
                   print(unit2 * 1000)
             if unit == 2:
                   unit2 = int(input("Enter the values (to conver g to kg): "))
                   print(unit2 / 1000)
             else:
                   print("Invalid input")      
       elif measurment == 3:
             print("1. hours", "2. minutes", "3. seconds")
             unit = int(input("Choose the unit you want to convert: "))
             if unit == 1:
                   print("1. seconds", "2. minutes")
                   unit2 = int(input("Which unit do you want to convert hours to: "))
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num * 3600)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num * 60)
                   else:
                         print("Invalid input")
             elif unit == 2:
                   print("1. hours", "2. seconds")
                   unit2 = int(input("Which unit do you want to convert minutes to: "))
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num / 60)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num * 60)
                   else:
                         print("Invalid input")
             
             elif unit == 3:
                   print("1. minutes", "2. hours")
                   unit2 = int(input("Which unit do you want to convert seconds to: "))
                   if unit2 == 1:
                         num = float(input("Enter the number: "))
                         print(num / 60)
                   elif unit2 == 2:
                         num = float(input("Enter the number: "))
                         print(num / 3600)      
                   else:
                         print("Invalid input")
 elif function == 3:
       print("1. Sine, 2. Cosine, 3. Tangent, 4. Secant, 5. Cosecant, 6. Cotangent")
       unit = int(input("Pick the trignometric function: "))
       if unit == 1:
             Sinetheta = float(input("Enter the value of the sine: "))
             print(sin(Sinetheta))
       elif unit == 2:
             Cosinetheta = float(input("Enter the value of the cosine: "))
             print(cos(Cosinetheta))
       elif unit == 3:
             Tangent = float(input("Enter the value of the tangent: "))
             print(tan(Tangent))
       elif unit == 4:
             Secant = float(input("Enter the value of the secant: "))
             print(acos(Secant)) 
       elif unit == 5:
             Cosecant = float(input("Enter the value of the cosecant: "))
             print(asin(Cosecant))
       elif unit == 6:
             Cotangent = float(input("Enter the value of the cotangent: "))
             print(atan(Cotangent))                 
       else:
             print("Invalid input")

      # Im not sure if the input is correct. so I will leave it for now
 
 
 elif function == 4:
       
       print("----------------------------------------------------------------")
       
       print("1. perimeter, area, volume, surface area")
       print("2. Speed, Distance, Time (or Velocity, Displacement, Time)")
       print("3. Binary, Hexadecimal, decimal, octal")

       convert = int(input("Choose the function you want to use: "))
       
       print("--------------------------------------------------------------------------------------------------")

       if convert == 1:
             print("1. perimeter")
             print("2. area")
             print("3. volume")
             print("4. surface area (under maintenance)")

             inp = int(input("Choose the measurment you want: "))

             if inp == 1:
                   
                   print("1. square, 2. rectangle, 3. circle, 4. triangle")
                   
                   shape = int(input("Choose the shape do you want: "))

                   if shape == 1:
                         num1 = float(input("Enter a side of the square: "))
                         print(num1*4)
                   elif shape == 2:
                         num1 = float(input("Enter the length of the rectangle: "))
                         num2 = float(input("Enter the breadth of the rectangle: "))
                         print(2*(num1 + num2))
                   elif shape == 3:
                         num1 = float(input("Enter the radius of the circle: "))
                         print(2*pi*num1)        
                   elif shape == 4:
                         num1 = float(input("Enter a side of the triangle: "))
                         num2 = float(input("Enter another side of the triangle: "))
                         num3 = float(input("Enter another side of the triangle: "))
                         print(num1 + num2 + num3)
                   else:
                         print("Invalid input")
                         break

             elif inp == 2:
                   print("1. square, 2. rectangle, 3. circle, 4. triangle")

                   shape = int(input("Choose the shape do you want: "))

                   if shape == 1:
                         num1 = float(input("Enter a side of the square: "))
                         print(num1**2)
                   elif shape == 2:
                         num1 = float(input("Enter the length of the rectangle: "))
                         num2 = float(input("Enter the breadth of the rectangle: "))
                         print(num1*num2)
                   elif shape == 3:
                         num1 = float(input("Enter the radius of the circle: "))
                         print(pi*num1**2)
                   elif shape == 4:
                         print("1. Equilateral Triangle") 
                         print("2. Right Triangle") 
                         print("3. Other Triangles (Herons Formula)")
                   else:
                         print("Invalid input")
                         break        

                         formula = int(input("Choose the formula: "))
                         if formula == 1:
                                side = float(input("Enter a side of the equilateral triangle: "))
                                print(sqrt(3)/4 * side**2)
                         elif formula == 2:
                               base = float(input("Enter the base of the right triangle: "))
                               height = float(input("Enter the height of the right triangle: "))
                               print(1/2*base*height) 
                         elif formula == 3:
                               s = float(input("Enter the half of the perimeter of the triangle:"))
                               a = float(input("Enter the first side of the triangle:"))
                               b = float(input("Enter the second side of the triangle:"))
                               c = float(input("Enter the third side of the triangle:"))
                               print(sqrt(s*(s-a)*(s-b)*(s-c)))
                         else:
                               print("Invalid input")
                               break      
             elif inp == 3:
                   print("1. cube, 2. cuboid, 3. sphere, 4. hemisphere, 5. cylinder, 6. cone")
                   shape = int(input("Choose the shape do you want: "))

                   if shape == 1:
                         num1 = float(input("Enter a side of the cube: "))
                         print(num1**3)
                   elif shape == 2:
                         num1 = float(input("Enter the length of the cuboid: "))
                         num2 = float(input("Enter the breadth of the cuboid: "))
                         num3 = float(input("Enter the height/depth of the cuboid: "))
                         print(num1*num2*num3)
                   elif shape == 3:
                         num1 = float(input("Enter the radius of the sphere: "))
                         print(4/3*pi*num1**3)
                   elif shape == 4:
                         num1 = float(input("Enter the radius of the hemisphere: "))
                         print(2/3*pi*num1**3)
                   elif shape == 5:
                         num1 = float(input("Enter the radius of the cylinder: "))
                         num2 = float(input("Enter the height of the cylinder: "))
                         print(pi*num1**2*num2) 
                   elif shape == 6:
                         num1 = float(input("Enter the radius of the cone: "))
                         num2 = float(input("Enter the height of the cone: "))
                         print(1/3*pi*num1**2*num2)
                   else:
                         print("Invalid input")
                         break            
             elif inp == 4:
                   print("1. sphere, 2. hemisphere, 3. cylinder, 4. cone, 5. cuboid, 6. cube")
                   surface = int(input("Choose the shape do you want: "))
                   if surface == 1:
                         num1 = float(input("Enter the radius of the sphere: "))
                         print(4*pi*num1**2)
                   elif surface == 2:
                         print("1. T.S.A or 2. C.S.A:") 
                         SA = float(input("Enter the one of the given options: "))
                         if SA == 1:
                               ans = float(input("Enter the radius of the hemisphere: "))
                               print(3*pi*ans**2)
                         elif SA == 2:
                               ans = float(input("Enter the radius of the hemisphere: "))
                               print(2*pi*ans**2)
                   elif surface == 3:
                         print("1. T.S.A or 2. C.S.A")
                         SA = float(input("Enter the one of the given options: "))
                         if SA == 1:
                               num1 = float(input("Enter the radius of the cylinder: "))
                               num2 = float(input("Enter the height of the cylinder: "))  
                               print(2*pi*num1*(num1 + num2))                           
                         elif SA == 2:
                               num1 = float(input("Enter the radius of the cylinder: "))
                               num2 = float(input("Enter the height of the cylinder: "))
                               print(2*pi*num1*num2)
                   elif surface == 4:
                         print("1. T.S.A or 2. C.S.A")
                         SA = float(input("Enter the one of the given options: "))
                         if SA == 1:
                          num1 = float(input("Enter the radius of the cone: "))
                          num2 = float(input("Enter the slant height of the cone (If you want to calculate it with height input 0): "))

                          if num2 == 0:
                               height = float(input("Enter the height of the cone"))
                               print(pi*num1*(sqrt(num1**2 + height**2)))
                          else:
                                print(pi*num1*num2)
                   elif surface == 5:
                         print("1. T.S.A or 2. L.S.A")  
                         SA = float(input("Enter the one of the given options: "))
                         if SA == 1:
                               num1 = float(input("Enter the height/depth of the cuboid: "))
                               num2 = float(input("Enter the length of the cuboid: "))
                               num3 = float(input("Enter the breadth of the cuboid: "))
                               print(2*(num2*num3)+(num3*num1)+ (num1*num2))
                         elif SA == 2:
                               num1 = float(input("Enter the height/depth of the cuboid: "))
                               num2 = float(input("Enter the length of the cuboid: "))
                               num3 = float(input("Enter the breadth of the cuboid: "))
                               print(2*(num2 +num3)*num1)
                   elif surface == 6:
                         print("1. T.S.A or 2. L.S.A") 
                         SA = float(input("Enter the one of the given options: "))
                         if SA == 1:
                               num = float(input("Enter the length of the cube: "))
                               print(6*num**2)
                         if SA == 2:
                               num = float(input("Enter the length of the cube: "))
                               print(4*num**2)
            

 elif function == 5:
       print("Thank you for using the calculator")
       break   
 else:
       print("Invalid function")
       retry = str(input("Do you want to try again? (y/n): "))
       if retry == "y":
             continue
       elif retry == "n":
             print("Thank you for using calculator pro max")
             break                                                           

#Boolean statement to check what operation they want to perform

 print("--------------------------------------------------------------------------------------------------")

 exit = str(input("Do you want to exit? (y/n): "))

 if exit == "n":
        continue
 
 elif exit == "y":
         print("Thank you for using the calculator")
         print("Someone hire me please")
         break
        
 else:
         print("Invalid input")
         break
        
# Finally the end of the program YAY!
# All I had to do is to while loop the whole program and use the 'continue' statement and 'break' statement
# After all that hard work, it is done (Until I realize no one wants to use the calculator)
