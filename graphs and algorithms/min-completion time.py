def minimize_completion_time(job_times):
    """
    Schedules jobs to minimize total completion time using a greedy algorithm.
    
    Args:
    job_times (list): List of processing times for jobs.
    
    Returns:
    int: The minimum total completion time.
    list: The optimal job schedule.
    """
    # Sort jobs by processing time (ascending)
    job_times.sort()
    
    # Calculate completion times
    total_time = 0
    completion_time = 0
    schedule = []
    
    for time in job_times:
        completion_time += time
        total_time += completion_time
        schedule.append(time)
    
    return total_time, schedule

# Example usage
job_times = [3, 5, 2, 8, 6]  # Example job processing times
total_time, schedule = minimize_completion_time(job_times)
print("Optimal Job Schedule (by processing time):", schedule)
print("Minimum Total Completion Time:", total_time)
