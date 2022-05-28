#!/usr/bin/#!/usr/bin/env python

import os
import sys

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)

main()
