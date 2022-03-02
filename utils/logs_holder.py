import os


class LogsHolder:
    logs = []

    def add_log(self, log: str):
        self.logs.append(log)

    def get_logs_str(self) -> str:
        str_logs:str = ""
        for log in self.logs:
            str_logs += log+"\n"

        return str_logs

    def get_logs(self):
        return self.logs

    def write(self, path):
        if os.path.exists(path):
            stream = open(path, "w")
            for line in self.logs:
                stream.write(line+"\n")

            stream.close()
