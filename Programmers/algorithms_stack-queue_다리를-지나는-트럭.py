def solution(bridge_length, weight, truck_weights):
    # answer = 0
    
    # count = 0
    
    
    # removelist = []
    # firsttruck = len(truck_weights)

    # while truck_weights:
    #     if len(truck_weights) == firsttruck:
    #         removed1 = truck_weights.pop(0)
    #         removelist.append(removed1)
    #         count += 1

    #     for 

    count = 0        
    arrived = []
    going = []
    firsttruck = len(truck_weights)
    while truck_weights:
        if len(truck_weights) == firsttruck:
            going.append(truck_weights.pop(0))
            count += 1


        for _ in range(len())
        if len(going) < bridge_length and sum(going) < weight:
            if sum(sum(going), truck_weights[0]) < weight:
                going.append(truck_weights.pop(0))
                count += 1
            else:
                count += 1
        else:
            count += 1
            going.clear()


    return count


bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
print(solution(bridge_length, weight, truck_weights))