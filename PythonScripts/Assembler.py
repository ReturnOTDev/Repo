import sys
import os

inp = input("Enter filename here: ")

file = open(os.path.join(sys.path[0], inp), "r")     # opening the assembly file
fline = file.readlines()
open("machineCode.hack", "w+").close()        # clears the machine code file

def mAnds(str, Ln):
    Ln = "".join(Ln)
    Ln = Ln.split(str)
    return Ln 

def change_char(s, p, r):
    return s[:p]+r+s[p+1:]

loc = 16      # next available location set to 16
count = 0   # program count set to 0
dic = {"SCREEN" : 16384,
        "KBD"   : 24576}    # setting up empty dictionary

isLine = True           # isLine set to True by default


for Ln in fline:            # ------------------------------- Setup for Symbol Dictionary ------------------------------ #

    Ln = Ln.strip()
    
    
    
    if not Ln.strip():
        count = count
    else:
        
        value = "".join(Ln[1:]).replace("\n", "")         # value is equal to everything after the @ sign


        if value.count("//"):
            value = value[0:value.index("/")]

        
                    # sets Sym to True if value is a symbol and not a number

        if Ln[1] == "R":
            count = count
        elif Ln[0] == "@":
        
            try:
                int(value)
                Sym = False
            except ValueError:
                Sym = True 
            

            if Sym and ((not(value in dic))):         # if value is a symbol and is not in the dictionary
                num = loc                           # assign number to value
                loc += 1                            # loc ++
                dic[value] = num                    # adds value to the dictionary
            count += 1
        
        elif (Ln[0] == "(") and (not(value in dic)):        # if it's a loop that has not been referenced
            value = value.replace(")", "")
            dic[value] = count                              # dictionary key is set to the next instruction


    
        else:
            count += 1      # count goes to next line of code
        


for i in fline:         # -------------------------------- MAIN - Instruction Handling ---------------------------------------- #
    
    Ln = list(i.strip())       # setting Ln to the active line of code
    
    if Ln.count("/"):
        Ln = Ln[0:Ln.index("/")]

 
    if not "".join(Ln).strip():
        count = count
    else:
        

        value = "".join(Ln[1:])


        try:
            int(value)
            S = False
        except ValueError:
            S = True

        

        if Ln[0] == "@":              # -------------------------------- A - Instruction Handling ---------------------------------------- #
            
            if Ln[1] == "R":
                num = int("".join(Ln[2::]))
            elif S:
                num = dic[value]
            else:
                num = int("".join(Ln[1::]))   # the number in int format


            binNum = str(bin(num)).split("b").pop()        # turns decimal into binary (without fron 0's)
            binNum = ("0" * (15-len(binNum))) + binNum           # adds in 0's
            code = "0" + binNum                      # final compiled machine code for line

            with open("machineCode.hack", "a") as f:
                f.write(code + "\n")            # adds the machine code to machineCode.txt and begins a new line
                f.close()                               


        elif not (Ln[0] == "("):                         # -------------------------------- C - Instruction Handling ---------------------------------------- #
            
            compBin = ""
            destBin = "000"
            jmpBin = "000"
            comp = []
            jmp = []
            dest = ""
            nd = True       # not disturbed = True

            if Ln.count("="):      # if the line has a comp function
                Ln = mAnds("=", Ln)        # merge and split from the = sign
                comp = Ln[1].strip()
                if Ln[1].count(";"):       # if the second part of the array has a ;
                    Ln.append(Ln[1].split(";"))              # splits the second half into two (comp and jump)
                    comp = Ln[2][0].strip()
                    jmp = Ln[2][1].strip()
                dest = Ln[0].strip()
            elif Ln.count(";"):
                Ln = mAnds(";", Ln)  
                jmp = Ln[1].strip()
                comp = Ln[0].strip()
            else:
                raise(Exception("\nError in code line: " + str(count-1) + ".\nPlease add a DEST or JMP to this line"))

            
            if dest.count("A"):
                destBin = change_char(destBin, 0, "1")
            if dest.count("D"):
                destBin = change_char(destBin, 1, "1")     # runs dest-Check to compile the dest bits
            if dest.count("M"):
                destBin = change_char(destBin, 2, "1")
            




                                # Algorithm for setting jmpBin value

            if jmp.count("JMP"):        
                jmpBin = "111"

            elif jmp.count("E"):
                jmpBin = change_char(jmpBin, 1, "1")             # sets middle bit to 1 if it is an equal jump
                
                if jmp.count("G"):
                    jmpBin = change_char(jmpBin, 2, "1") 
                elif jmp.count("L"):        
                    jmpBin = change_char(jmpBin, 0, "1") 
                elif jmp.count("N"):
                    jmpBin = "101"          
            
            else:

                if jmp.count("G"):
                    jmpBin = change_char(jmpBin, 2, "1") 
                elif jmp.count("L"):        
                    jmpBin = change_char(jmpBin, 0, "1")          # sets corresponding bits to their jump values





            a = "0"
                                            # Algorithm for setting compBin value
            
            

            if comp.count("M"):     # if it is an M comp instruction
                a = "1"
                comp = comp.replace("M", "A")       # replace M with A

            A = comp.count("A")     # True if comp has A
            D = comp.count("D")     # True if comp has D

            
            if len(comp) <= 2:
                if not (D or A):
                    
                    if comp == "0":
                        compBin = "101010"  
                        
                    elif comp == "-1":
                        compBin = "111010"

                    elif comp == "1":
                        compBin = "111111"
                else:
                    if A:
                            compBin = "110000"
                    elif D:
                            compBin = "001100"
                        
                    if comp.count("-"):
                            compBin = change_char(compBin, 4, "1")
                            compBin = change_char(compBin, 5, "1")
                    elif comp.count("!"):
                        compBin = change_char(compBin, 5, "1")

            elif D and A:
                
                if comp == ("D+A") or ("A+D"):
                    compBin = "000010"
                elif comp == "D-A":
                    compBin = "010011"
                elif comp == "A-D":
                    compBin = "000111"
                elif comp == "D|A":
                    compBin = "010101"
                elif comp == ("D&A") or ("A&D"):
                    compBin = "000000"
                
            else:
                if D:
                    compBin = "011111"
                    if comp.count("-"):
                        compBin = "001110"
                elif A:
                    compBin = "110111"
                    if comp.count("-"):
                        compBin = "110010"

            code = "111" + a + compBin + destBin + jmpBin

            with open("machineCode.hack", "a") as f:
                f.write(code + "\n")
                f.close()

input("\n\nAssembler has finished\nPress enter to close")