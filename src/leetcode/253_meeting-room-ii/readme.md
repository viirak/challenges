# Problem 253. Meeting Rooms II
<https://leetcode.com/problems/meeting-rooms-ii/>

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

**Example 1:**

    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: 2

**Example 2:**

    Input: intervals = [[7,10],[2,4]]
    Output: 1

**Constraints:**

* 1 <= intervals.length <= 104
* 0 <= starti < endi <= 106

**Python Solution I**

First, sort the meetings by their starting time. Then iterate the meeting list and have a list to track the ongoing meetings ordering by ended time, if the meeting start time is greater than the first ongoing meeting ending time, remove the first meeting and append the meeting. If the meeting start time is less than the first ongoing meeting ending time, append the meeting. We can use a heap to help maintain the ongoing meeting orders.

    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            meetings = []

            intervals = sorted(intervals, key=lambda interval:interval[0])
            heapq.heappush(meetings, intervals[0][1])

            for interval in intervals[1:]:   
                if interval[0] >= meetings[0]:
                    heapq.heappop(meetings)
                    heapq.heappush(meetings, interval[1])
                else:
                    heapq.heappush(meetings, interval[1])
            return len(meetings)

**Python Solution II**
We can list all meeting starting times and ending times as events. We then sort the events by time. If encountering a start event, we increase the count, otherwise, we decrease the count.

    class Event:

        def __init__(self, time, is_start):
            self.time = time
            self.is_start = is_start

    class Solution:
        def minMeetingRooms(self, intervals: List[List[int]]) -> int:
            events = []

            for interval in intervals:
                events.append(Event(interval[0], 1))
                events.append(Event(interval[1], 0))
            events = sorted(events, key=lambda event: (event.time, event.is_start))
            count = 0
            room_needed = 0
            for event in events:
                if event.is_start:
                    count += 1
                else:
                    count -= 1
                room_needed = max(room_needed, count)
            return room_needed

Time Complexity: ~Nlog(N)
Space Complexity: ~N
