def solution(food_times, k):
    foods = len(food_times)
    if k < foods :
        return k + 1

    if k >= sum(food_times) :
        return -1

    min_time = min(food_times)
    cycle = k // foods
    if cycle < min_time :
        return (k % foods) + 1

    times = sorted(list(enumerate(food_times)), key = lambda x : (x[1], x[0]))
    # print(times)
    temp = 0

    while True :
        key, value = times.pop(0)
        k = k - ((value - temp) * (len(times) + 1))
        # print(value, times[0][1])
        while value == times[0][1] :
            times.pop(0)
        temp = value
        cycle = k // len(times)
        if cycle < times[0][1] - value :
            break

    keys = [key + 1 for key, value in times]
    keys.sort()
    # print(keys, k % len(times))
    return keys[k % len(times)]

food_times = [1,1,1,1]
solution(food_times, 4)
