 // multiplies values R0 and R1, outputs at R2
@R1
D=M
@i
M=D

 (LOOP)
 @i
 D=M
 @END
 D;JEQ      // if R1 == 0 goto END

 @R0
 D=M
 @R2
 M=D+M      // R2 += R0

 @i
 M=M-1      // R1--

 @LOOP
 0;JMP      // goto LOOP


 (END)
 @END
 0;JMP      // END OF PROGRAM