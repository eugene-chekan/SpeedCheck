#  Copyright (c) 2023. Yauheni Chekan

"""Module with classes and methods for application client."""

import speedtest


class SpeedCheckClient:
    """Implementation of the SpeedCheck client."""

    def __init__(self):
        self.test = speedtest.Speedtest()
        # If you want to test against a specific server: servers = [1234]
        self.servers = []
        self._threads = None  # If you want to use a single threaded test threads = 1

    @property
    def threads(self):
        return self._threads

    @threads.setter
    def threads(self, threads_number: int):
        self._threads = threads_number
