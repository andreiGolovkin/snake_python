import time


class Timer:
    def __init__(self, interval: float):
        self.interval = interval
        self.start_time = time.time()

    def restart(self):
        self.start_time = time.time()

    def is_triggered(self) -> bool:
        current_time = time.time()

        return current_time - self.start_time >= self.interval

    def is_finished(self) -> bool:
        ans = self.is_triggered()

        if ans:
            self.restart()

        return ans
