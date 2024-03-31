def EDRR_algorithm(processes, burst_times):
    BTmax = max(burst_times)
    
    QT = 0.8 * BTmax
    
    remaining_processes = []
    
    N = len(processes)
    
    arrival_time = 0
    
    
    turn_aroundtime = 0
    completion_time = 0
    total_waiting_time = 0  
    
    for i in range(N):
        if burst_times[i] <= QT:
            completion_time += burst_times[i]  
            turn_aroundtime += completion_time - arrival_time  
            waiting_time = completion_time - arrival_time - burst_times[i]  
            total_waiting_time += waiting_time 
            print("Process", "Waiting Time:", waiting_time)
        else:
            remaining_processes.append(burst_times[i])  

    if remaining_processes:
        QT = BTmax  
        
        for burst_time in remaining_processes:
            completion_time += burst_time 
            turn_aroundtime += completion_time - arrival_time  
            waiting_time = completion_time - arrival_time - burst_time 
            total_waiting_time += waiting_time 
            print("Remaining Process", "Waiting Time:", waiting_time)

    average_waiting_time = total_waiting_time / N  
    print("Average Waiting Time:", average_waiting_time)
    average_turnaround_time = turn_aroundtime / N 
    print("Average Turnaround Time:", average_turnaround_time)


processes = [1, 2, 3, 4, 5]
burst_times = [80, 45, 62, 34, 78]

EDRR_algorithm(processes, burst_times)
