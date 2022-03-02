from datetime import datetime, timedelta


MICRO_IN_MILI = 1000


class Stopwatch:
    start_time: datetime = None
    stop_time: datetime = None
    diff: timedelta = None

    def start(self):
        # reset from previous measurement
        self.stop_time = None
        self.diff = None

        self.start_time = datetime.now()

    def stop(self):
        self.stop_time = datetime.now()

        self.diff = self.stop_time - self.start_time

    def seconds(self) -> int:
        if self.diff != None:
            return int(self.diff.seconds)

        return 0

    def milliseconds(self) -> int:
        if self.diff != None:
            return int(self.diff.microseconds / MICRO_IN_MILI)

        return 0

    def microseconds(self) -> int:
        if self.diff != None:
            return int(self.diff.microseconds % MICRO_IN_MILI)

        return 0

    def get_time_str(self) -> str:
        s = self.seconds()
        ms = self.milliseconds()
        mc = self.microseconds()

        message = str(f"s:{s} ms:{ms} mc:{mc}")

        return message
