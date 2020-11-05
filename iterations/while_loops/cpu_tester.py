# CPU Tester, Ryan Kelley, v0.1
import time

start_time = time.time()
x = 0
while x < 1000:
    x += 1
    print(f"{x:,}\n")
end_time = time.time()
print(f"It took {end_time - start_time} seconds to count up to {x}.")
time.sleep(5)

start_time = time.time()
x = 0
while x < 1000:
    x = x + 1
    print(f"{x:,}\n")
end_time = time.time()
print(f"It took {end_time - start_time} seconds to count up to {x}.")
