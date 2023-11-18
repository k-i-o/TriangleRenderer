import math
import turtle
  
def getInputs():
    return int(input("First side: ")), int(input("Second side: "))

def getHypothenuse(var1, var2):
    return math.sqrt(math.pow(var1, 2) + math.pow(var2, 2))

def getAngle(var1, var2, var3):
    return (math.acos((math.pow(var2, 2)+math.pow(var3, 2)-math.pow(var1, 2))/(2*var2*var3)))*180/3.14159265359

def getAngles(var1, var2, var3):
    return getAngle(var1, var2, var3), getAngle(var2, var1, var3), getAngle(var3, var1, var2)

def drawIt(var1, var2, var3, var4, var5):

    constant = 180

    board = turtle.Turtle()

    board.forward(var2) # draw base
    
    board.left(constant-var5)
    board.forward(var1)
    
    board.left(constant-var4)
    board.forward(var3)
    
    turtle.done()

def main():
    
    a, b = getInputs()

    print("\n----------------------------------\n")

    c = getHypothenuse(a, b)

    print("Found the hypothenuse of the triangle")
    print("Formula = √(A^2 + B^2)")
    print(f"Side A is {a} cm ")
    print(f"Side B is {b} cm ")
    print(f"Hypotenuse C is {round(c, 2)} cm ")

    print("\n----------------------------------\n")

    alpha, beta, gamma = getAngles(a, b, c)

    print("Alpha: " + str(round(alpha, 2)))
    print("Beta: " + str(round(beta, 2)))
    print("Gamma: " + str(round(gamma, 2)))

    print("\n----------------------------------\n")

    print("Drawing the triangle...")
    drawIt(a, b, c, beta, gamma)

if __name__ == '__main__':
    main()