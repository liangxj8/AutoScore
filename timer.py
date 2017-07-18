# coding=utf-8
import time
import sched
from main import main

s = sched.scheduler(time.time, time.sleep)


def perform(sec=60):
    s.enter(sec, 0, perform, (sec,))
    now = time.strftime('%Y.%m.%d %H:%M', time.localtime(time.time()))
    print(now)
    main()


if __name__ == "__main__":
	# operate every 10 minutes
    perform(600)
    s.run()
