def EDRR_algorithm(processes, arrival_times, burst_times):
    process_data = list(zip(processes, arrival_times, burst_times))
    
    process_data.sort(key=lambda x: x[2])
    
    BTmax = max(burst_times)
    QT = 0.8 * BTmax
    N = len(processes)
    
    turn_aroundtime = 0
    completion_time = 0
    total_waiting_time = 0
    
    for process, arrival_time, burst_time in process_data:
        if burst_time <= QT:
            completion_time += burst_time
            turn_aroundtime = completion_time - arrival_time
            waiting_time = turn_aroundtime - burst_time
            total_waiting_time += waiting_time
           
        else:
            QT = BTmax
            completion_time += burst_time
            turn_aroundtime = completion_time - arrival_time
            waiting_time = turn_aroundtime - burst_time
            total_waiting_time += waiting_time
            
    
    average_waiting_time = total_waiting_time / N
    print("Average Waiting Time:", average_waiting_time)




processes = [1, 2, 3, 4, 5]
arrival_times = [0, 5, 8, 15, 20]
burst_times = [45, 90, 70, 38, 55]

EDRR_algorithm(processes, arrival_times, burst_times)
