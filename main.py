from teamtime import TeamTime
import sys

main, filename = sys.argv

new_time = TeamTime()
new_time.read(filename)
print(new_time.get())
