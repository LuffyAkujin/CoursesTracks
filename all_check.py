#!/usr/bin/#!/usr/bin/env python

import os

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():
    pass

main()