def circle_function () :
    print("")
    print("Circle Function")
    print("")

    input1= (input("Enter Parameter: "))
    input2= (input("Enter Parameter: "))
    input3= (input("Enter Parameter: "))
    input4= (input("Enter Parameter: "))
    input5= (input("Enter Parameter: "))



    print(f"Area of the Circle = {(3.14159 * (int(input2)) ** 2):.1f}")
    print(f"Area of the Circle = {(3.14159 * (int(input3)) ** 2):.2f}")
    print(f"Area of the Circle = {(3.14159 * (int(input4)) ** 2):.2f}")
    print(f"Area of the Circle = {(3.14159 * (int(input5)) ** 2):.2f}")
    print("")
    print("")


circle_function()




def tax_function() :
    print("")
    print("Tax Function")
    print("")
    tax1= int(input("Money Before Tax: "))
    tax2= int(input("Money Before Tax: "))
    tax3= int(input("Money Before Tax: "))

    print(f"Total Due: ${(tax1 * 1.06):.2f}")
    print(f"Total Due: ${(tax2 * 1.04):.2f}")
    print(f"Total Due: ${(tax3 * 1.08):.2f}")
    print("")
    print("")

tax_function()

def temp_function () :
    print("")
    print("Temperature Function")
    print("")
    temp1= (input("Enter the temperature in Fahrenheit: "))
    temp2= (input("Enter the temperature in Fahrenheit: "))
    temp3= (input("Enter the temperature in Fahrenheit: "))
    temp4= (input("Enter the temperature in Fahrenheit: "))

    print (f" Temperature in Celsius = {(int(temp1) -32) * 5/9:.0f}")
    print (f" Temperature in Celsius = {(int(temp2) -32) * 5/9:.4f}")
    print (f" Temperature in Celsius = {(int(temp3) - 32) * 5/9:.4f}")
    print (f" Temperature in Celsius = {(int(temp4) - 32) * 5/9:.5f}")


temp_function()