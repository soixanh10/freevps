import time
import sys

start = time.time()
try:
    while True:
        elapsed = int(time.time() - start)
        sys.stdout.write(f"Elapsed: {elapsed} seconds\n")
        sys.stdout.flush()
        time.sleep(60)
except KeyboardInterrupt:
    pass
