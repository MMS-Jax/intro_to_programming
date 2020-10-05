if light == green:
    drive.forward
    speed.limit
elif light == yellow:
    drive.forward
    speed.slow_down
elif light == red:
    speed.stop
else:
    speed.slow_down
    drive.pull_over
