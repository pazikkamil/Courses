def clock_angle(time):
    hours, minutes = map(int, time.split(":"))
    if (hours > 13):
        hours - 12
    minutesHand = minutes * 6
    hoursHand = hours * 30 + minutes * 0.5
    
    angleDiff = abs(minutesHand - hoursHand)
    complementDiff = abs(360 - angleDiff)
    if ( complementDiff < angleDiff ):
        return complementDiff
    else:
        return angleDiff


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")

