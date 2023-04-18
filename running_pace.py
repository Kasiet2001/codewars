def running_pace(distance, time):
    time = time.split(':')
    pace_sec = (int(time[0]) * 60 + int(time[1]))/distance
    pace = f'{int(pace_sec//60)}:{int(pace_sec % 60)}'
    if len(pace.split(':')[1]) == 1:
        return f'{int(pace_sec//60)}:0{int(pace_sec % 60)}'
    return pace
print(running_pace(5,'25:00'))