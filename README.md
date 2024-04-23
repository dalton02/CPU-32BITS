##   Circuit Overview

The Logisim-implemented circuit embodies vital components intricately linked to craft a robust 32-bits processor architecture. These components collaboratively facilitate instruction execution. Leveraging pipeline circuits, instructions are segmented, enhancing code performance by segregating each operation's execution phase.

<img src="/preview.png" height="500" alt="Preview"  />

## How to code:

### OPCODES:
- **0000** - ADD
- **0001**  - SUB
- **0010**  - MULT
- **0011**  - DIVISION
- **0100**  - AND OPERATION
- **0101**  - OR OPERATION
- **1000**  - Load immediate
- **1001**  - Save in Memory
- **1010**  - Load in Memory
- **1011**  - JUMP
- **1100**  - IF EQUAL
- **1101**  - IF LESS OR EQUAL THAN
### Instructions Example:


-   **ADD RX RY RZ:** Adds the content of RX and RY and stores the result in RZ.
-   **SUB RX RY RZ:** Subtracts the content of RY from RX and stores the result in RZ.
-   **LI RX 12:** Saves the value 12 in register RX.
-   **SW RX RY:** Saves the content of RY in the memory address specified by RX.
-   **LW RX RY:** Loads the content from the memory address specified by RX into register RY.
-   **JUMP RD:** Jumps to the memory address specified by RD.
-   **IF R1 R2 RD:** If R1 is equal to R2, jumps to the memory address specified by RD.

### Usage Examples:

-   **Memory Test Function:**
    
    -   LI R1 10
    -   LI R2 5
    -   SW R0 R1
    -   LW R0 R3
    -   ADD R3 R1 R2
-   **Condition Test Function:**
    
    -   LI R0 0
    -   LI R1 10
    -   SW R0 R1
    -   LW R0 R2
    -   ADD R1 R1 R1
    -   IF EQUAL R1 R2 R0
-   **Sum Test Function:**
    
    -   LI R0 10
    -   LI R1 5
    -   ADD R1 R0 R0
    -   MULT R1 R0 R1
    -   SUB R1 R0 R2
