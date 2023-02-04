import random as r

def randomnumber(upper):
    num = r.randint(1,upper)
    return num

def main():
    repeat =True
    num1 = randomnumber(5)
    num2 = randomnumber(5)
    output = num1 + num2

    while repeat:
        ans = input("enter the sum of "+ str(num1)+ "+" + str(num2))

        if ans.isdigit():
            if int(ans)==output:
                print("you have entered the correct number! congrats")
                repeat = False
            else:
                print("you have entered the wrong number")
        else:
            print("you have entered the incorrect number ")

if __name__=='__main__':
    main()