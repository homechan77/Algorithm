def solution(routes):
    # 진출 시점을 기준으로 정렬
    routes.sort(key=lambda x:x[1])
    # 차량의 진입 지점은 최대가 -30000이므로 -30001부터 시작
    camera_location = -30001
    camera_count = 0
    
    # 정렬된 routes를 반복하며 현재의 카메라 위치가 진입 시점보다 작은 경우 해당 차량을 찍지 못하기 때문에
    # 카메라를 추가로 설치하여 주어야 하는데 그 위치는 진출 시점으로 한다.
    for i in routes:
        if camera_location < i[0]:
            camera_count += 1
            camera_location = i[1]
    
    return camera_count

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))
