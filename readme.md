copilot_test.py is a Python script that displays your system's uptime. It works on Unix-like systems (such as Linux) by reading from /proc/uptime, and falls back to using the uptime command for other environments. If neither method is available, it will report that it is unable to determine system uptime.

How It Works
On Linux: Reads /proc/uptime to calculate and print the number of hours, minutes, and seconds since the system was last started.
On other systems: Attempts to use the uptime shell command and prints its output.
If neither method works, prints an error message.
