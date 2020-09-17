def saving_people(people, limit):
    people.sort()
    left = 0
    right = len(people)-1
    boats = 0

    while(left <= right):
        if(left == right):
            boats = boats + 1
            break

        if(people[left]+people[right] <= limit):
            left = left + 1

        right = right - 1
        boats = boats + 1

    return boats


people = [1, 2, 3, 3]
limit = 3
how_many_boats_needed = saving_people(people, limit)

print(how_many_boats_needed)
