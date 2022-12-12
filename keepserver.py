import subprocess
import os
import signal

server = subprocess.Popen(["python", "server.py"])
pid = server.pid
import time

t = 0
print('Start Server Condition Detecting...')
while True:
    t += 1
    if server.poll() is not None or t % 60 == 0:
        # server.py has stopped running, so close it and reopen it
        os.kill(pid, signal.SIGTERM)
        print("Killed server.py")
        server = subprocess.Popen(["python", "server.py"])
        pid = server.pid

    # check again in a few seconds
    time.sleep(60)