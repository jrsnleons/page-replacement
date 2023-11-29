from tabulate import tabulate, SEPARATING_LINE

def userinput():
    pagestr = input("Inpuut Page String (add space between):")
    frames = int(input("Input number of Frames: "))
    
    pages = pagestr.split()
    
    return (pages, frames)

def fifo(pages, frames):
    i = 1
    # counters 
    hit = 0
    fault = 0
    table = [["Time"]]  
    
    # creates the header of the frames
    for i in range(1, frames+1):
        table.append(["F" + str(i)])
        for x in range(1, len(pages)+1):
            table[i].append(' ')                 
        i+=1
    
    # init time array
    for x in range(1, len(pages)+1):
        table[0].append(str(x))
        
    # init page hit and fault array
    table.append([SEPARATING_LINE])
    table.append(["H/F"])
    
        
    # fifo calculation
    q = []
    x = 0   #index of last 
    for i in range(0, len(pages)):
        if len(q) < frames:
            # for the first 3 
            if not pages[i] in q:
                q.append(pages[i])
                table[-1].append('F')
                fault += 1
            else:
                table[-1].append('H')
                hit += 1
                pass
        else:
            if not pages[i] in q:
                x = x % frames
                q[x] = pages[i]
                x = x + 1
                table[-1].append('F')
                fault += 1
            else:
                table[-1].append('H')
                hit += 1
                pass
        
        # store to table
        for z in range(1, frames + 1):
            if z <= len(q):
                table[z][i + 1] = q[z - 1]
    
    avgF = (fault/len(pages))*100
    avgH = (hit/len(pages))*100
    
    # display the resuuts
    print("\n===== OUTPUT TABLE =====\n")
    print(tabulate(table, headers = "firstrow"))
    print(f"\nFaults: \t{fault}")
    print(f"Hits: \t\t{hit}")
    print(f"Average Fault: \t{avgF:.2f}%")
    print(f"Average Hit: \t{avgH:.2f}%")
    
    
    return()

def main():
    print("First In First Out Algorithm")
    pages, frames = userinput()
    fifo(pages, frames)

tabulate


main()




# TODO
# - fix the frames and all



        # if len(q) == 1:
        #     table[1][i+1] = q[0]
        # elif len(q) == 2:
        #     table[1][i+1] = q[0]
        #     table[2][i+1] = q[1]
        # elif len(q) == 3:
        #     for z in range(1, frames+1):
        #         table[z][i+1] = q[z-1]