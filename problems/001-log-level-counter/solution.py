def count_log_levels(lines: list[str]) -> dict[str, int]:
    """Return a mapping of log level -> number of valid lines at that level."""
    counts = {}
    statuses = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    for log in lines:
        cleanedLog = log.strip()
        splitLog = cleanedLog.split(" ")
        if len(splitLog) < 3:
            continue
        upperStatus = splitLog[2].upper()
        if upperStatus not in statuses:
            continue
        if upperStatus not in counts:
            counts[upperStatus] = 0
        counts[upperStatus]+=1
    return counts
     
    
