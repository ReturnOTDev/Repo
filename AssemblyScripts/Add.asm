// Counts from value of RAM[0] onward
// Usage: set RAM[0] to a value then run

@R0     // set register 0's value to data register
D=M

D=D+1   // D++

@R1     // set register 1 to the value of D
M=D

@2      // infinite loop back to step 2
0;JMP