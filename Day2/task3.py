def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

time_str = "24:59:59"
print(time_to_seconds(time_str)) 
