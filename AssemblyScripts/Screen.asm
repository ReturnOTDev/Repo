// Creates a rectangle, 16 pixels wide with a length of R0. set offset to (horizontal R1 and vertical R2)

@R0
D=M
@n
M=D     // n = R0

@R1
D=M
@horizontal
M=D     // horizontal offset = R1

@R2
D=M
@vertical
M=D     // vertical = R2

@1
D=A
@i
M=D     // i = 1

@SCREEN
D=A
@horizontal
D=D+M
@base
M=D     // base = A(Screen) + horizontal


(FIRSTLOOP)
@0
D=A
@vertical
D=M-D
@SECONDLOOP
D;JEQ      // if vertical == 0 goto SECONDLOOP

@32
D=A
@base
M=M+D       // base += 32

@vertical
M=M-1       // vertical--

@FIRSTLOOP
0;JMP       // goto FIRSTLOOP


(SECONDLOOP)
@n
D=M
@i
D=D-M
@END
D;JEQ       // if i == n goto END

@base
A=M
M=-1        // RAM[base] = -1

@32
D=A
@base
M=D+M       // base += 32

@i
M=M+1       // i++

@LOOP
0;JMP


(END)
@END
0;JMP       // END OF PROGRAME