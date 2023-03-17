def format_time(seconds):
    """Formats a time duration in seconds as a string in the format h.min.sec"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):d}:{int(minutes):02d}:{int(seconds):02d}"

if __name__ == "__main__":
    pass