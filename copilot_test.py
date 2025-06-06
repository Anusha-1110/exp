import os

  def print_system_uptime():
      # On Unix-like systems, uptime is available via /proc/uptime
      try:
          with open('/proc/uptime', 'r') as f:
              uptime_seconds = float(f.readline().split()[0])
              hours = int(uptime_seconds // 3600)
              minutes = int((uptime_seconds % 3600) // 60)
              seconds = int(uptime_seconds % 60)
              print(f"System Uptime: {hours}h {minutes}m {seconds}s")
      except FileNotFoundError:
          # For non-Linux systems, fallback to using uptime command
          try:
              uptime = os.popen('uptime').read()
              print("System Uptime:", uptime.strip())
          except Exception as e:
              print("Unable to determine system uptime:", e)

  if __name__ == "__main__":
      print_system_uptime()
