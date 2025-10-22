# Server Log Analyzer
This is Python Script Analyzes Server Log, Each Log Entry has timestamp,log leve,message.
Written 4 Functions to accomplish this task.

# test_file
This function for Read & Parse the file
# count_log_level
This function for "Count the number of occurrences of each log level (INFO, WARNING, ERROR, DEBUG)"
# find_recent_log
This function for "Find the most recent log entry for a given log level"
# filter_logs_by_date
This function for "Filter logs by a user-specified date range and save the filtered logs to a file"

`<timestamp>`: `YYYY-MM-DD HH:MM:SS`
`<log_level>`: `INFO`, `WARNING`, `ERROR`, or `DEBUG`
 `<message>`: Description of the log entry

**Example (`logs.txt`):**

1. **Read & Parse Logs**
   - Reads `logs.txt`
   - Skips empty or malformed lines

2. **Count Log Levels**
   - Counts occurrences of each log level
   - Displays a summary to the user

3. **Find Most Recent Log Entry**
   - Shows the user for a log level
   - Finds and displays the most recent entry of that level according to use input

4. **Filter Logs by Date Range**
   - Prompts the user for start and end dates (`YYYY-MM-DD`)
   - Acquire all logs within that range
   - Saves filtered logs to `filtered_logs.txt`

# How can we Run ?
make sure `log_analyzer.py` and `logs.txt` should be in same folder.

# Assumptions

1) The log file is in plain text with each log on a new line. intentionally added empty line in logs.txt file because how it will handle the code, which what if
   **if not line:** in **test_file** function.

2) Timestamps always follow the format YYYY-MM-DD HH:MM:SS.

3) Only four log levels are recognized: INFO, WARNING, ERROR, DEBUG.

4) Malformed or empty lines are skipped, not processed.


# AUTHOR
**PundariKaksha.B**
