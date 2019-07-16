@SCREEN
D=A
@base
M=D     // base = A[SCREEN]

@24576
D=A
@lastSCR
M=D         //lastSCR = 24576

@i
M=0

(FIRST)
@KBD
D=M
@SEC
D;JGT       // if KBD = any value goto SEC

@i
D=M
@base
D=D+M
A=D
M=0        // base+i = 0 (white pixels)

@i
M=M-1      // i--

@FIRST
0;JMP       // goto FIRST

(SEC)

@KBD
D=M
@FIRST
D;JEQ       // if KBD = no value go to FIRST

@base
D=M
@i
D=D+M
@lastSCR
D=D-M
@SEC
D;JEQ       // if lastSCR - (current base value) == 0 goto FIRST

@i
D=M
@base
D=D+M
A=D
M=-1        // base+i = -1 (black pixels)

@i
M=M+1       // i++

@FIRST
0;JMP       // goto SEC



