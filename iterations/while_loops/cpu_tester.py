# CPU Tester, Ryan Kelley, v0.1
import time

for i in range(3):
    start_time0 = time.time()
    x = 0
    while x < 100:
        x += 1
        print(f"{x:,}\n")
    end_time0 = time.time()
    print(f"It took {end_time0 - start_time0} seconds to count up to 1,000.\n")
    time.sleep(5)

    start_time1 = time.time()
    while x != 0:
        x += -1
        print(f"{x:,}\n")
    end_time1 = time.time()
    print(f"It took {end_time1 - start_time1} seconds to count down from 1,000.\n")
    print(f"This is loop {i + 1}.")
    time.sleep(3)
    
    
