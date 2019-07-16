@20

D=A
@basePoint
M=D

@i
M=0

(LOOP)
@KBD
D=M
@basePoint
A=M
M=D

@i
M=M+1

D=M
@basePoint
D=D+M
M=D

@LOOP
0;JMP
