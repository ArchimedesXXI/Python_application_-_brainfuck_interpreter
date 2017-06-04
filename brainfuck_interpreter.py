#import sys

def interpret_bf_code(bf_code, memory_size = 30000):
    '''
    (str, (int)) -> str

    This function interprets code in the BrainFuck language,
    which is passed in via bf_code parameter
    and returns the output of executing that code.
    If so specified in BrainFuck code, the function reads input from user.
    '''
    
    instruction_PTR = 0
    memory_PTR = memory_size // 2
    memory = [0] * memory_size
    Output = ""
    
    while instruction_PTR < len(bf_code):        
        ch = bf_code[instruction_PTR]

        if ch == '>':
            memory_PTR = (memory_PTR + 1) % memory_size;

        elif ch == '<':
            memory_PTR = (memory_PTR - 1) % memory_size;

        elif ch == '+':
            memory[memory_PTR] = memory[memory_PTR] + 1;

        elif ch == '-':
            memory[memory_PTR] = memory[memory_PTR] - 1;

        elif ch == '.':
            # chr(int) -> char   converts int to a char with corresponding ASCII code
            out_ch = chr( memory[memory_PTR] )
            Output = Output + out_ch
        elif ch == ',':
            # ord(char) -> int   converts char to its corresponding ASCII code
            in_ch = input("Input 1 byte in form of a single character: ")
            memory[memory_PTR] = ord(in_ch[0])

        elif ch == '[':
            if memory[memory_PTR] == 0:
                loops = 1
                while loops > 0:
                    instruction_PTR +=1
                    if bf_code[instruction_PTR] == '[':
                        loops += 1
                    elif bf_code[instruction_PTR] == ']':
                        loops -= 1

        elif ch == ']':
            loops = 1
            while loops > 0:
                instruction_PTR -=1
                if bf_code[instruction_PTR] == '[':
                    loops -= 1
                elif bf_code[instruction_PTR] == ']':
                    loops += 1
            instruction_PTR -= 1

        instruction_PTR +=1

    print(Output)
    return Output



#if len(sys.argv) >= 2:
#    bf_code = sys.argv[1]
#    interpret_bf_code(bf_code)
    
if __name__ == "__main__":
	bf_test_code = input("Type in BrainFuck code: ")
	interpret_bf_code(bf_test_code)
