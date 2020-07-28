#!/usr/bin/env python3

'''
Console-based text editor trainer.

Run this with no arguments. It will print directions and a file to
open, then measure how long it takes you from opening the file to
writing the correct results.
'''

import fswatch
import os
import random
import sys
import tempfile
import time


# https://github.com/emcrisostomo/fswatch/blob/44bafcbf0a89a36c5e87aba805a4af9c600187b9/libfswatch/src/libfswatch/c/cevent.h#L67
CREATED_FLAG = 1 << 1
# https://github.com/emcrisostomo/fswatch/blob/44bafcbf0a89a36c5e87aba805a4af9c600187b9/libfswatch/src/libfswatch/c/cevent.h#L68
UPDATED_FLAG = 1 << 2


class Challenge(object):
    ''' Container for original text, expected text, and instructions. '''
    def __init__(self, original_text, expected_text, instructions):
        self.original_text = original_text
        self.expected_text = expected_text
        self.instructions = instructions

    def write(self, path):
        with open(path, 'w') as fout:
            fout.write(self.original_text)

    def verify(self, path):
        ''' Return True if the challenge was correctly edited. '''
        try:
            with open(path, 'r') as fin:
                contents = fin.read()
        except:
            return False
        return contents == self.expected_text


CHALLENGES = [Challenge("cawcawcawcawcaw",
                        "cowcowcowcowcow",
                        "Replace all the 'a's with 'o's.")]


def main():
    ''' Run the main loop. '''
    (_, tmpname) = tempfile.mkstemp()
    try:
        challenge = random.choice(CHALLENGES)
        challenge.write(tmpname)
        start_time = time.time()
        print('Open "{}".'.format(tmpname))
        print(challenge.instructions)

        monitor = fswatch.Monitor()
        monitor.add_path(tmpname)

        def callback(path, evt_time, flags, flags_num, event_num):
            end_time = evt_time
            # TODO: Filter out first callback.
            if UPDATED_FLAG & flags_num:
                if challenge.verify(tmpname):
                    print('Finished in {}'.format(end_time - start_time))
                    # TODO: Actually do sane program exit.
                    sys.exit(0)
                else:
                    print('Not quite... keep trying...')
        monitor.set_callback(callback)
        monitor.start()
    finally:
        try:
            os.remove(tmpname)
        except:
            pass


if __name__ == '__main__':
    main()
