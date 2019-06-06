f = open("newtext.txt")
(f.readline())
(f.readline())
(f.readline())
(f.readline())

count = len(f.readlines(  ))
print count

f.close()
f = open("newtext.txt")

f.readline()
f.readline()
f.readline()
f.readline()

lineslists = []
for x in range (0, count):
	lineslists.append(f.readline())
lineslists.sort()

newLines = []

for x in lineslists:
	newLines.append("2, " + x) 

newLines2 = []

for x in newLines:
	newLines2.append(x.replace("N", "Note_on_c"))

	#print(x.replace("N", "Note_on_c"))
	#for y in x:
	#	pass
newLines3 = []

for x in newLines2:
	newLines3.append(x.replace("C", "Control_c"))


newLines4 = []
for x in newLines3:
	newLines4.append(x.replace("_c", "_c, 0"))

for x in newLines4:
	print x

fout = open("sample2midi.txt", "w")

fout.write("0, 0, Header, 1, 2, 480 \n1, 0, Start_track \n1, 0, Key_signature, 0, \"major\" \n1, 0, SMPTE_offset, 96, 0, 0, 0, 0\n1, 0, Tempo, 500000\n1, 0, Time_signature, 4, 2, 24, 8\n1, 0, End_track\n2, 0, Start_track\n")
for x in newLines4:
	fout.write(x)


parameters = newLines4[-1].split(",")

print parameters

fout.write("2, " + parameters[1] + ", End_track\n")
fout.write("0, 0, End_of_file")