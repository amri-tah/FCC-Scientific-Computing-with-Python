def add_time(start, duration, day=None):
    start_time, start_am_pm = start.split(" ")
    start_hour, start_min = start_time.split(":")
    dur_hour, dur_min = duration.split(":")
    start_hour, start_min, start_am_pm = int(start_hour), int(start_min), start_am_pm.upper()
    dur_hour, dur_min = int(dur_hour), int(dur_min)

    # Convert start to 24hr clock
    if start_am_pm == "PM":
        start_hour += 12

    # Calculating end time
    end_hour = start_hour + dur_hour
    end_min = start_min + dur_min
    if end_min >= 60:
        end_hour += end_min // 60
    end_min = end_min % 60
    if (end_hour % 24) <= 11:
        end_am_pm = "AM"
    else:
        end_am_pm = "PM"
    end_day = end_hour // 24
    # final hours as per 12-Hour clock
    end_hour = (end_hour % 24) % 12

    # Formatting output
    if end_hour == 0:
        end_hour = 12
    if end_min <= 9:
        end_min = "0" + str(end_min)
    end_time = f"{str(end_hour)}:{str(end_min)} {end_am_pm}"
    if day:
        days_dict = {"Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6, "Saturday": 0, "Sunday": 1}
        day_name = (days_dict[day.title()] + end_day) % 7
        for i, j in days_dict.items():
            if j == day_name:
                day_name = i
                break
        if end_day == 0:
            return end_time + ', ' + day_name
        if end_day == 1:
            return end_time + ', ' + day_name + ' (next day)'
        return end_time + ', ' + day_name + ' (' + str(
            end_day) + ' days later)'
    else:
        if end_day == 0:
            return end_time
        if end_day == 1:
            return end_time + " (next day)"
        return end_time + f" ({end_day} days later)"

