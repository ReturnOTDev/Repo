// sets an array of registers from 100 up to 110, to the value of -1

@100
D=A
@arr
M=D     // arr = 100

@10
D=A
@n
M=D     // n = 10

@i
M=0     // i = 0

(LOOP)
@i
D=M
@n
D=M-D
@END
D;JEQ       // if i == n goto END

@arr
D=M
@i
A=D+M       // set A register to location of i + arr

M=-1        // set that register to -1

@i
M=M+1       // i++

@LOOP
0;JMP       // goto LOOP

(END)
@END
0;JMP       // END OF PROGRAME