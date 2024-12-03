input = open("input.txt", "r")
lines = input.readlines()

total = 0

for line in lines:
    for i in range(0, len(line)-8):
        if(line[i:i+4] == "mul("):
            factor1find = False
            factor2find = False
            for j in range(3, 0, -1):
                start1 = i+4

                try:
                    factor1 = int(line[start1:start1+j])
                    factor1find = True

                except ValueError:
                    factor1find = False
                
                separator = start1+j

                if(line[separator] != ","):
                    factor1find = False
                
                start2 = separator+1

                if(factor1find):
                    for l in range(3, 0, -1):
                        try:
                            factor2 = int(line[start2:start2+l])
                            factor2find = True

                        except ValueError:
                            factor2find = False
                        
                        terminator = start2+l

                        if(factor2find and line[terminator] == ")"):
                            total = total + factor1 * factor2
                            break

                if(factor1find and factor2find):
                    continue


print(total)