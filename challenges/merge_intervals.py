def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merge_interval_start = intervals[0][0]
    merge_interval_end = intervals[0][1]

    output = []

    for curr_interval in intervals[1:]: 
        if curr_interval[0] <= merge_interval_end:
            merge_interval_end = max(merge_interval_end, curr_interval[1])
        else:
            output.append([merge_interval_start, merge_interval_end])
            merge_interval_start = curr_interval[0]
            merge_interval_end = curr_interval[1]

    output.append([merge_interval_start, merge_interval_end])
    return output
