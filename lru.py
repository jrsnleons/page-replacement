from tabulate import tabulate, SEPARATING_LINE

def userinput():
    pagestr = input("Input Page String (add space between): ")
    frames = int(input("Input number of Frames: "))
    
    pages = pagestr.split()
    
    return (pages, frames)

def lru(pages, frames):
    # counters 
    hit = 0
    fault = 0
    table = [["Time"]]  
    
    # creates the header of the frames
    for i in range(1, frames+1):
        table.append(["F" + str(i)])
        for x in range(1, len(pages)+1):
            table[i].append(' ')                 
        i += 1
    
    # init time array
    for x in range(1, len(pages)+1):
        table[0].append(str(x))
        
    # init page hit and fault array
    table.append([SEPARATING_LINE])
    table.append(["H/F"])
    
    # LRU calculation
    q = []
    time = {}  # Dictionary to store the time of last access for each page
    current_time = 0
    for i in range(0, len(pages)):
        current_time += 1
        
        if len(q) < frames:
            # for the first 'frames' pages
            if pages[i] not in q:
                q.append(pages[i])
                time[pages[i]] = current_time
                table[-1].append('F')
                fault += 1
            else:
                time[pages[i]] = current_time
                table[-1].append('H')
                hit += 1
        else:
            if pages[i] not in q:
                # Find the page with the least recent access time
                min_time_page = min(q, key=lambda x: time[x])
                q[q.index(min_time_page)] = pages[i]
                time[pages[i]] = current_time
                table[-1].append('F')
                fault += 1
            else:
                time[pages[i]] = current_time
                table[-1].append('H')
                hit += 1
        
        # store to table
        for z in range(1, frames + 1):
            if z <= len(q):
                table[z][i + 1] = q[z - 1]
    
    avgF = (fault / len(pages)) * 100
    avgH = (hit / len(pages)) * 100
    
    # display the results
    print("\n===== OUTPUT TABLE =====\n")
    print(tabulate(table, headers="firstrow"))
    print(f"\nFaults: \t{fault}")
    print(f"Hits: \t\t{hit}")
    print(f"Average Fault: \t{avgF:.2f}%")
    print(f"Average Hit: \t{avgH:.2f}%")

def main():
    print("Least Recently Used (LRU) Algorithm")
    pages, frames = userinput()
    lru(pages, frames)

main()
