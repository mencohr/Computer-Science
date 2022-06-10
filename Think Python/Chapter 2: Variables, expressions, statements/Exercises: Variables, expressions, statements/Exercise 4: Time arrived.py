"""Current time if someone starts at 6:52 a.m.:
runs one mile at 8:15, three miles at 7:12, one mile at 8:15."""
start_hr = 6                        # Start time in sec
start_min = 52

start_time_sec = ((start_hr * 60) * 60) + (start_min * 60)

min_ran = 8 + (7 * 3) + 8           # Time ran in sec
sec_ran = 15 + (12 * 3) + 15
total_ran_sec = (min_ran * 60) + sec_ran

end_time_sec = start_time_sec + total_ran_sec
end_time = str((end_time_sec // 60) // 60) + ":" + str((end_time_sec // 60) % 60)

print("Someone starts at", (str(start_hr) + ":" + str(start_min) + ":"), "\n",
      "runs for", (str(min_ran) + " min,"), (str(sec_ran) + " sec,"), "\n",
      "end time is", str(end_time))