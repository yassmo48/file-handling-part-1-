file = open("notes.txt", "r")


print(file.read(20))
file.close()




file = open("notes.txt","r")
lines = file.readlines()
file.close()

print("total lines", len(lines))

for i in range(len(lines)):
    print(i +1, "->", lines[i].strip())


word = input("Skip lines starting with   ")
file=open("notes.txt", "r")

for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()



file = open("notes.txt","r")
lines = file.readlines()
file.close()

out=open("oddlines.txt", "w")

for i in range(0,len(lines), 2):
    out.write(lines[i])





out.close()

file=open("oddlines.txt", "r")
print(file.read())
file.close()

print("odd lines saved to odd lines")