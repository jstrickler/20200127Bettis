#!/usr/bin/env python


class FRDFile():
    def __init__(self, file_name):
        self._file_name = file_name

    def get_requirements(self):
        return {}


if __name__ == '__main__':
    ff = FRDFile('/path/to/frd1001.frd')

    rl = ff.get_requirments()

