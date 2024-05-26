def sjf_scheduling(jobs, service_times):
    # Create a list of tuples (job, service_time) and sort based on service time
    job_service_times = sorted(zip(jobs, service_times), key=lambda x: x[1])
    
    total_time = 0
    schedule = []

    for job, service_time in job_service_times:
        start_time = max(total_time, job)  # Ensures non-negative start time
        total_time = start_time + service_time
        schedule.append((job, start_time, total_time))

    return schedule, total_time

if _name_ == "_main_":
    jobs = [1, 5, 2, 10]
    service_times = [3, 7, 4, 8]

    schedule, total_time = sjf_scheduling(jobs, service_times)

    print("SJF Schedule:")
    print("Job\tStart Time\tEnd Time")
    for job, start_time, end_time in schedule:
        print(f"{job}\t{start_time}\t\t{end_time}")
    print(f"Total Time Spent: {total_time}")
