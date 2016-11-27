with open("finalGrades.txt", 'r') as f:
    my_list = [line.rstrip(u'\n') for line in f]
itc = [0, 0, 0, 0, 0]
dsp = [0, 0, 0, 0, 0]
micro = [0, 0, 0, 0, 0]
ctrl = [0, 0, 0, 0, 0]
cult = [0, 0, 0, 0, 0]
Btp = [0, 0, 0, 0, 0]
for line in my_list:
	if line[20] == "A":
		itc[0] += 1
	elif line[20] == "B":
		itc[1] += 1
	elif line[20] == "C":
		itc[2] += 1
	elif line[20] == "D":
		itc[3] += 1
	elif line[20] == "F":
		itc[4] += 1
	if line[30] == "A":
		dsp[0] += 1
	elif line[30] == "B":
		dsp[1] += 1
	elif line[30] == "C":
		dsp[2] += 1
	elif line[30] == "D":
		dsp[3] += 1
	elif line[30] == "F":
		dsp[4] += 1	
	if line[40] == "A":
		micro[0] += 1
	elif line[40] == "B":
		micro[1] += 1
	elif line[40] == "C":
		micro[2] += 1
	elif line[40] == "D":
		micro[3] += 1
	elif line[40] == "F":
		micro[4] += 1
	if line[50] == "A":
		ctrl[0] += 1
	elif line[50] == "B":
		ctrl[1] += 1
	elif line[50] == "C":
		ctrl[2] += 1
	elif line[50] == "D":
		ctrl[3] += 1
	elif line[50] == "F":
		ctrl[4] += 1		
	if line[60] == "A":
		cult[0] += 1
	elif line[60] == "B":
		cult[1] += 1
	elif line[60] == "C":
		cult[2] += 1
	elif line[60] == "D":
		cult[3] += 1
	elif line[60] == "F":
		cult[4] += 1	
	if line[70] == "A":
		Btp[0] += 1
	elif line[70] == "B":
		Btp[1] += 1
	elif line[70] == "C":
		Btp[2] += 1
	elif line[70] == "D":
		Btp[3] += 1
	elif line[70] == "F":
		Btp[4] += 1	
print "ITC:",itc, "DSP:",dsp, "MICRO:",micro, "CONTROL:",ctrl, "CULTURE:",cult, "BTP:",Btp


#20, 30, 40, 50, 60, 70