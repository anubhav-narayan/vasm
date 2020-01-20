import sys
import re
label_regex=r'(?<=:)[\s\t]+'
comm_regex=r'[\dLS],\d{1,2}'
MOT={
"1":["STOP","ADD","SUB","MULT","MOVR","MOVM","COMP","BC","DIV","READ","PRINT"],
"2":["","DS","DC"],
"3":["","START","END","ORG","EQU","LTORG"],
"4":["","AREG","BREG","CREG","DREG"],
"5":["","EQ","LT","GT","LE","GE","NE","ANY"]
}
REG_BANK=[0,0,0,0,0]
FLAGS_BANK={"ZERO":0,"SIGN":0}
MEM_BANK={}
LT={}
ST={}
LC=0
LTC=0
IC=""
def tokenise(line=""):
	line=re.sub(label_regex,"\n\t",line)
	line=line.split('\n')
	for x in range(0,len(line)):
		line[x]=line[x].strip('\t')
		line[x]=line[x].split(' ')
		for y in range(0,len(line[x])):
			line[x][y]=line[x][y].split(',')
			pass
		pass
	return line
	pass
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
def reg_handler(lex=""):
	if lex in MOT["4"]:
		pass_over="<4,"+str(MOT["4"].index(lex))+">"
		pass
	else:
		pass_over="\t"
		pass
	return pass_over
	pass
def coder(code=""):
	mcode=re.findall(comm_regex,code)
	code_len=len(mcode)
	if code_len==1:
		if mcode[0][0]=='1' and mcode[0][2]=='0':
			return
			pass
		pass
	if code_len==2:
		if mcode[0][0]=='1':
			if mcode[0][2]=='9':
				var=int(input())
				MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=var
				pass
			if mcode[0][2]=='1':
				print(MEM_BANK[list(ST.keys())[int(mcode[1][2])]])
				pass
			pass	
		pass
	if code_len==3:
		if mcode[0][0]=='1':
			if mcode[0][2]=='1':
				if mcode[1][0]=='4' and mcode[2][0]=='4':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]+REG_BANK[int(mcode[2][2])]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='S':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]+MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='L':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]+int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			if mcode[0][2]=='2':
				if mcode[1][0]=='4' and mcode[2][0]=='4':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]-REG_BANK[int(mcode[2][2])]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='S':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]-MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='L':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]-int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			if mcode[0][2]=='3':
				if mcode[1][0]=='4' and mcode[2][0]=='4':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]*REG_BANK[int(mcode[2][2])]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='S':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]*MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='L':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]*int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			if mcode[0][2]=='8':
				if mcode[1][0]=='4' and mcode[2][0]=='4':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]/REG_BANK[int(mcode[2][2])]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='S':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]/MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[1][0]=='4' and mcode[2][0]=='L':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[1][2])]/int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			if mcode[0][2]=='4':
				if mcode[2][0]=='4':
					REG_BANK[int(mcode[1][2])]=REG_BANK[int(mcode[2][2])]
					pass
				if mcode[2][0]=='S':
					REG_BANK[int(mcode[1][2])]=MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[2][0]=='L':
					REG_BANK[int(mcode[1][2])]=int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			if mcode[0][2]=='5':
				if mcode[2][0]=='4':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=REG_BANK[int(mcode[2][2])]
					pass
				if mcode[2][0]=='S':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[2][0]=='L':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			pass
		if mcode[1][0]=='2':
			if mcode[1][2]=='1':
				MEM_BANK[list(ST.keys())[int(mcode[0][2])]]=int(list(LT.keys())[int(mcode[2][2])])
				pass
			pass
		if mcode[0][0]=='5':
			if mcode[0][2]=='1':
				if mcode[2][0]=='4' and  mcode[1][0]=='4':
					if REG_BANK[int(mcode[1][2])]==REG_BANK[int(mcode[2][2])]:
						FLAGS_BANK["ZERO"]=1
						pass
					pass
				if mcode[2][0]=='S' and  mcode[1][0]=='4':
					if REG_BANK[int(mcode[1][2])]==MEM_BANK[list(ST.keys())[int(mcode[2][2])]]:
						FLAGS_BANK["ZERO"]=1
						pass
					pass
				if mcode[2][0]=='L' and  mcode[1][0]=='4':
					if REG_BANK[int(mcode[1][2])]==int(list(LT.keys())[int(mcode[2][2])]):
						FLAGS_BANK["ZERO"]=1
						pass
					pass
				if mcode[2][0]=='4' and mcode[1][0]=='S':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=REG_BANK[int(mcode[2][2])]
					pass
				if mcode[2][0]=='S' and mcode[1][0]=='S':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=MEM_BANK[list(ST.keys())[int(mcode[2][2])]]
					pass
				if mcode[2][0]=='L' and mcode[1][0]=='S':
					MEM_BANK[list(ST.keys())[int(mcode[1][2])]]=int(list(LT.keys())[int(mcode[2][2])])
					pass
				pass
			pass
		pass
	pass
def code_map(lex=[],lt=0,lex_len=0):
	global LTC
	icode=""
	if lex[0][0] in MOT["1"]:
		tabcode=MOT["1"].index(lex[0][0])
		opcode="<1,"+str(tabcode)+">"
		if tabcode==1:#ADD
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			elif lex[1][0] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])
				pass
			else:
				icode=opcode+"\t"
				pass
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])+"\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==2:#SUB
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			elif lex[1][0] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])
				pass
			else:
				icode=opcode+"\t"
				pass
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])+"\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==3:#MULT
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			elif lex[1][0] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])
				pass
			else:
				icode=opcode+"\t"
				pass
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])+"\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==8:#DIV
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			elif lex[1][0] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])
				pass
			else:
				icode=opcode+"\t"
				pass
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])+"\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==4:#MOVR
			icode=opcode+reg_handler(lex[1][0])
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==5:#MOVM
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			else:
				ST[lex[1][0]]=lt
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
				pass
			if lex[1][1] in ST.keys():
				icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
				pass
			elif lex[1][1] in MOT["4"]:
				icode=icode+reg_handler(lex[1][1])+"\n"
				pass
			elif check_int(lex[1][1]):
				LT[lex[1][1]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==9:
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">\n"
				pass
			elif lex[1][0]:
				ST[lex[1][0]]=lt
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">\n"
				pass
			else:
				icode=opcode+"\t\n"
				pass
		if tabcode==10:
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">\n"
				pass
			elif lex[1][0] in MOT["4"]:
				icode=opcode+reg_handler(lex[1][0])+"\n"
				pass
			elif lex[1][0]:
				LT[lex[1][0]]=lt
				icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][0]))+">\n"
				pass
			else:
				icode=opcode+"\t\n"
				pass
			pass
		pass
	elif lex[0][0] in MOT["3"]:
		tabcode=MOT["3"].index(lex[0][0])
		opcode="<3,"+str(tabcode)+">"
		if tabcode==1:#START
			LTC=int(lex[1][0])-1
			LT[lex[1][0]]=LTC
			icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][0]))+">\n"
			pass
		if tabcode==2:#END
			icode="<3,2>\n"
			pass
		if tabcode==3:#ORG
			if lex[1][0] in ST.keys():
				icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">\n"
				pass
			if lex[1][0] in LT.keys():
				icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][0]))+">\n"
				pass
			elif check_int(lex[1][0]):
				LT[lex[1][0]]=lt
				icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][0]))+">\n"
				pass
			else:
				icode=icode+"\t\n"
				pass
			pass
		if tabcode==5:#LTORG
			pool_counter=LTC
			for x in LT.keys():
				LT[x]=pool_counter
				pool_counter=pool_counter+1
				pass
			pass
		pass
	elif lex[0][0] in MOT["5"]:
		tabcode=MOT["5"].index(lex[0][0])
		opcode="<5,"+str(tabcode)+">"
		if lex[1][0] in ST.keys():
			icode=opcode+"<S,"+str(list(ST.keys()).index(lex[1][0]))+">"
			pass
		elif lex[1][0] in LT.keys():
			icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][0]))+">"
			pass
		elif lex[1][0] in MOT["4"]:
			icode=opcode+reg_handler(lex[1][0])
			pass
		elif check_int(lex[1][1]):
			LT[lex[1][1]]=lt
			icode=opcode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">"
			pass	
		else:
			icode=opcode+"\t"
			pass
		if lex[1][1] in ST.keys():
			icode=icode+"<S,"+str(list(ST.keys()).index(lex[1][1]))+">\n"
			pass
		elif lex[1][1] in LT.keys():
			icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
			pass
		elif lex[1][1] in MOT["4"]:
			icode=icode+reg_handler(lex[1][1])+"\n"
			pass
		elif check_int(lex[1][1]):
			LT[lex[1][1]]=lt
			icode=icode+"<L,"+str(list(LT.keys()).index(lex[1][1]))+">\n"
			pass
		else:
			icode=icode+"\t\n"
			pass
		pass
	elif lex[1][0] in MOT["2"]:
		tabcode=MOT["2"].index(lex[1][0])
		opcode="<2,"+str(tabcode)+">"
		if tabcode==1:
			ST[lex[0][0]]=lt
			icode="<S,"+str(list(ST.keys()).index(lex[0][0]))+">"+opcode
			if lex[2][0] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
				pass
			else:
				LT[lex[2][0]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
				pass
			pass
		if tabcode==2:
			ST[lex[0][0]]=lt
			icode="<L,"+str(list(LT.keys()).index(lex[0][0]))+">"+opcode
			if lex[2][0] in LT.keys():
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
				pass
			else:
				LT[lex[2][0]]=lt
				icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
				pass
			pass
		pass
	elif lex[1][0] in MOT["3"]:
		opcode="<3,4>"
		ST[lex[0][0]]=(int(lex[2][0]),lt)
		icode="<S,"+str(list(ST.keys()).index(lex[0][0]))+">"+opcode
		if lex[2][0] not in LT.keys():
			LT[lex[2][0]]=lt
			icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
			pass
		else:
			icode=icode+"<L,"+str(list(LT.keys()).index(lex[2][0]))+">\n"
			pass
		pass
	else:
		icode="\t"
		pass
	return icode
	pass
if '-h' in sys.argv or len(sys.argv)==1:
	print("Usage : vasm.py <filename> <options>")
	print("OPTIONS:-")
	print("-h : Help")
	print("-d : Debug Info")
	pass
else:
	file=open(sys.argv[1],"r")
	batch=file.read()#Get the Lines
	line=tokenise(batch)
	for x in line:
		line_len=len(x)
		if line_len==1:
			if x[0][0]!="END":
				ST[x[0][0].strip(':')]=LTC
				pass
			else:
				IC=IC+code_map(x,lt=LTC)
				pass
			pass
		elif line_len==2:
			IC=IC+code_map(x,lt=LTC)
			pass
		elif line_len==3:
			IC=IC+code_map(x,lt=LTC)
			pass
		else:
			print("error",end=" ")
			print(x)
			pass
		LTC=LTC+1
		LC=LC+1
		pass
	if '-p1' not in sys.argv:
		S_IC=IC.split('\n')
		for x in S_IC:
			coder(x)
			pass
		pass
	pass
# '''
# Data Structures
# '''
if '-d' in sys.argv:
	print(ST)
	print(LT)
	print(LC)
	print(LTC)
	print(REG_BANK)
	print(MEM_BANK)
	print(IC)
	pass
