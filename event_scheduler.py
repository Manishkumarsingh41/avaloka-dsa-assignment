import heapq


def can_attend_all(events):
    events = sorted(events)

    for i in range(1, len(events)):
        if events[i][0] < events[i - 1][1]:
            return False

    return True


def min_rooms_required(events):
    if not events:
        return 0

    events = sorted(events)
    room_ends = []

    for start, end in events:
        while room_ends and room_ends[0] <= start:
            heapq.heappop(room_ends)

        heapq.heappush(room_ends, end)

    return len(room_ends)
