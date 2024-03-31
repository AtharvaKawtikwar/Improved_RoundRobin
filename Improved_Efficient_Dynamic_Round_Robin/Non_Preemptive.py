def EDRR_algorithm(processes, burst_times):
    BTmax = max(burst_times)
    
    QT = 0.8 * BTmax
    
    N = len(processes)
    arrival_time=0
    burst_times.sort()
    turn_aroundtime = 0
    i = 0

    completion_time = 0
    total_waiting_time = 0
    
    while i < N:
        if i < N:
            if burst_times[i] <= QT:
                completion_time += burst_times[i]
                turn_aroundtime=completion_time-arrival_time
                waiting_time=turn_aroundtime-burst_times[i]
                total_waiting_time += waiting_time
                print(waiting_time)

                
            elif burst_times[i] > QT:
                QT=BTmax
                completion_time+=burst_times[i]
                turn_aroundtime=completion_time-arrival_time
                waiting_time=turn_aroundtime-burst_times[i]
                total_waiting_time += waiting_time
                print(waiting_time)

                
        i += 1
    
    average_waiting_time = total_waiting_time / N
    print("Average Waiting Time:", average_waiting_time)
   


processes = [1, 2, 3, 4, 5]
burst_times = [80, 45, 62, 34, 78]

EDRR_algorithm(processes, burst_times)


