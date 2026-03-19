def main():
    #ask for number and check if number is divisible by 20
    userNum = int(input("Enter in a number please that is divisible by 20:"))
    if not userNum % 20 == 0:
        print(f" {userNum} is not divisible by 20!")
    else:
        # prompt user for the other information required
        userFloat = float(input("Enter in a floating point number"))
        userFamilyMember = input("Enter in a singular family member")
        userNoun = input("Enter in a noun")
        userAdjective = input("Enter in a adjective")
        # print everything required for the lab
        print(f"{(int)(userNum / 20)} score and {userFloat:.3f} years ago, our fore{userFamilyMember}s brought forth upon this {userNoun} a {userAdjective} nation.")
if __name__ == "__main__":
    main()
