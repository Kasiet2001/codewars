def to_time(seconds):
    return f'{seconds // 3600} hour(s) and {(seconds % 3600) // 60} minute(s)'
print(to_time(0))