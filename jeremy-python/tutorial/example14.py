file = open("alice.txt","r")
text = file.readlines()
file.close()

file2 = open ("output.txt", "w")
file2.writelines(text)
file2.close

file2 = open ("append.txt", "a")
file2.writelines(text)
file2.close
