"""Miles per hour of 10-km race in 42 min, 42 sec"""
miles = 10 / 1.61             # Km to miles
sec = (60 * 42) + 42            # Sec in 42 min, 42 sec
sec_per_mile = sec / miles    # Sec per mile averaged
mph = 60 / (sec_per_mile / 60)  # Mph

# "%.2f" %
## "" = string formatting
## "%" = placeholder for string values
## .2 = 2 decimal points
## f = floating point indicator
## % = modulo operater for answer with string formatting
print ("10-km race at 42 min, 42 sec is", ("%.2f" % mph), "mph")