import numpy as np

def avg_travel_time(location, location2, timetableEntries):
    distances = []
    
    for start_loc, start_date, arr_loc, arr_date in timetableEntries:
        if start_loc == location and arr_loc == location2:
            distances.append(int(arr_date) - int(start_date))
        elif start_loc == location2 and arr_loc == location:
            distances.append(int(arr_date) - int(start_date))

    return np.mean(distances) if distances else -1.0

if __name__ == "__main__":
    loc = input()
    loc2 = input()
    n = int(input())
    m = int(input())
    timetable = [input().split() for _ in range(n)]
    print(avg_travel_time(loc, loc2, timetable))


#------------------EXAMPLE 1 INPUT------------------#
# A
# B
# 4
# 4
# A 1 B 2
# B 3 A 5
# A 1 C 3
# C 5 D 12
#-----------------EXAMPLE 1 OUTPUT-----------------#
# 1.5
