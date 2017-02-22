
def min_time_for(required_distance, data):
    last = len(data) - 1

    def count_time_for(curr_distance, head=-1, tail=-1, curr_min_time=None):
        while curr_distance < required_distance and head is not last:
            head += 1
            curr_distance += data[head]

        while curr_distance >= required_distance:
            tail += 1
            curr_distance = curr_distance - data[tail]

            if curr_distance < required_distance:
                if curr_min_time is not None:
                    curr_min_time = min(curr_min_time, head - tail + 1)
                else:
                    curr_min_time = head - tail + 1

        if head == last and curr_distance < required_distance:
            if curr_min_time is None:
                raise ValueError(
                    "Required distance can't be greater then path length")
            return curr_min_time
        else:
            return count_time_for(curr_distance, head, tail, curr_min_time)

    return count_time_for(0)
    pass
