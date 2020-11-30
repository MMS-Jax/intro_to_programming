import time
x = 0
start_time = time.time()

while x < 1000000:
    x += 1
    print(f"{x:,}\n")

end_time = time.time()
print(f"The time taken was {start_time - end_time} seconds.\n")

    
