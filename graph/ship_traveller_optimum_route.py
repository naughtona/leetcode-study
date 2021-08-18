from heapq import heappush, heappop
from collections import defaultdict

"""
    10 Islands A-J.
    Starting from A, find the earliest one can visit all islands (A-J).
    Besides the start location, route can take any order and does not need to finish at J.
    Return an array of strings, representing the order in which the islands \
    should be visited to achieve the optimum route (starting with A).
"""

def find_optimum_route(timetableEntries):
    adj_list = defaultdict(list)
    
    # fill adjacency list
    for start_loc, start_date, arr_loc, arr_date in timetableEntries:
        adj_list[start_loc] += [(arr_loc, int(start_date), int(arr_date))]
    
    # priority queue implemented as minheap
    minheap = [(0, [False]*9, ["A"])] # (travel time, mask of visited, chronology of visits)
    while minheap:
        # pop the node with the shortest travel time from p-queue
        curr_arrival, mask, visited = heappop(minheap)
        curr_island = visited[-1]
        
        # have we visited all islands yet?
        if all(mask):
            return visited
        
        # add the neighbouring islands to the p-queue
        for isl, depart, arrive in adj_list[curr_island]:
            # but only if the ship departs a day after they arrived
            if curr_arrival < depart:
                # update mask with visit to `isl`
                new_mask = mask.copy()
                if isl != 'A' and not mask[ord(isl) - ord('B')]:
                    new_mask[ord(isl) - ord('B')] = True
                # push new node onto p-queue
                heappush(minheap, (arrive, new_mask, visited + [isl]))
    
    # if we get here, there is no path from A that visits all islands B-J :(
    return None

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    timetable = [input().split() for _ in range(n)]
    print(find_optimum_route(timetable))


#----------------EXAMPLE 1 INPUT----------------#
# 9	
# 4
# A 1 B 2
# B 3 C 4
# C 5 D 6
# D 7 E 8
# E 9 F 10
# F 11 G 12
# G 13 H 14
# H 15 I 16
# I 17 J 18
#--------------EXAMPLE 1 OUTPUT-----------------#
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
