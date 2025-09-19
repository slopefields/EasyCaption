def format_time(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    centiseconds = round((time - int(time)) * 100)
    return f"{hours}:{minutes:02}:{seconds:02}.{centiseconds:02}"