with open("Animals.txt","r") as file:
    for line in file:
        if "cats" in line:
            line = line.replace("cats","🐈cats🐈")
            print(line.strip())