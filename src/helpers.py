import time

def format_time(seconds):
    """Formats a time duration in seconds as a string in the format h.min.sec"""
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours):d}:{int(minutes):02d}:{int(seconds):02d}"

def time_it(func):
    is_evaluating = False
    def g(x):
        nonlocal is_evaluating
        if is_evaluating:
            return func(x)
        else:
            start_time = time.time()
            is_evaluating = True
            try:
                value = func(x)
            finally:
                is_evaluating = False
            end_time = time.time()
            print('Sudoku solved in: {time:.2f} seconds'.format(time=end_time-start_time))
            return value
    return g


if __name__ == "__main__":
    pass