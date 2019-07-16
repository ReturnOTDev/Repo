// Adds all values from 1 up to R0 together
// Usage: input value at R0

@R0
D=M
@n          
M=D         // n = R0
@Sum
M=0         // Sum = 0
@i
M=1         // i = 1

(LOOP)
@i
D=M
@n
D=D-M
@STOP
D;JGT      // if i > n, goto STOP

@i
D=M
@Sum
M=D+M      // Sum += i

@i
M=M+1      // i++

@LOOP
0;JMP      // goto LOOP

(STOP)
@Sum
D=M
@R1
M=D       // R1 = Sum

(END)
@END
0;JMP      // Coninuous end loop