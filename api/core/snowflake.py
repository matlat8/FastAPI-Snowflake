

class Snowflake:
    def __init__(self, snowflake_id: int):
        self.snowflake_id = snowflake_id
        self.timestamp = (snowflake_id >> 22) + 1420070400000
        self.worker_id = (snowflake_id & 0x3E0000) >> 17
        self.process_id = (snowflake_id & 0x1F000) >> 12
        self.increment = snowflake_id & 0xFFF

    def __str__(self):
        return f"Snowflake ID: {self.snowflake_id}\nTimestamp: {self.timestamp}\nWorker ID: {self.worker_id}\nProcess ID: {self.process_id}\nIncrement: {self.increment}"