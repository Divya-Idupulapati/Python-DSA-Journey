import time

my_time = int(input("Enter the time in seconds:"))

for i in reversed(range(0, my_time)):
    seconds = i % 60
    minutes = (i % 3600) // 60
    hours = i // 3600
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time's UP")
