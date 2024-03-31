def EDRR_algorithm(processes, arrival_times, burst_times):
    BTmax = max(burst_times)
    QT = 0.8 * BTmax
    
    remaining_processes = []
    
    N = len(processes)
    
    total_waiting_time = 0
    total_turnaround_time = 0
    
    process_data = list(zip(processes, arrival_times, burst_times))
    process_data.sort(key=lambda x: x[1])  
    
    current_time = 0
    process_index = 0
    
    while process_index < N:
        process, arrival_time, burst_time = process_data[process_index]
        
        if arrival_time <= current_time:  
            if burst_time <= QT:  
                current_time += burst_time
                turnaround_time = current_time - arrival_time
                waiting_time = turnaround_time - burst_time
                total_waiting_time += waiting_time
                total_turnaround_time += turnaround_time
                print(f"Process {process}: Waiting Time: {waiting_time}")
                process_index += 1
            else:  
                remaining_processes.append((process, arrival_time, burst_time))
                process_index += 1
        else:  
            if remaining_processes: 
                next_process, next_arrival, next_burst = remaining_processes.pop(0)
                current_time = max(current_time, next_arrival)  
                process_data.append((next_process, next_arrival, next_burst))  
            else:  
                current_time = arrival_time
    

    for process, arrival_time, burst_time in remaining_processes:
        current_time += burst_time
        turnaround_time = current_time - arrival_time
        waiting_time = turnaround_time - burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        print(f"Process {process}: Waiting Time: {waiting_time}")
    

    average_waiting_time = total_waiting_time / N
    average_turnaround_time = total_turnaround_time / N
    
    print("Average Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)


processes = [1, 2, 3, 4, 5]
arrival_times = [0, 5, 8, 15, 20] 
burst_times = [45, 90, 70, 38, 55]

EDRR_algorithm(processes, arrival_times, burst_times)
