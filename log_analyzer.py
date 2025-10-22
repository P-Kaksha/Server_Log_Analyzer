from collections import Counter
from datetime import datetime
def test_file(file_path='logs.txt'):
    logs=[]
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                if len(line)<19:
                    print(f"WARNING skipping malformed line:{line}")
                    continue 
                timestamp=line[:19] 
                rest=line[20:].strip()
                if ' ' not in rest:
                    print(f"skipping malformed line")
                log_level,message=rest.split(None,1)
                logs.append((timestamp,log_level,message))
        
    except FileNotFoundError:
       return(' log file not found')
    return logs

def count_log_levels(logs):
    levels=[log[1] for log in logs]
    counts=Counter(levels)
    for level in ["INFO","WARNING","ERROR","DEBUG"]:
        print(f"{level}: {counts.get(level,0)}")

def find_recent_log(logs):
    log_level=input('enter a log level ').upper()
    filtered_log=[log for log in logs if log[1]==log_level]
    if not filtered_log:
        print('no log level found')
    most_recent_log=max(filtered_log,key=lambda log:datetime.strptime(log[0],"%Y-%m-%d %H:%M:%S"))
    print(' '.join(most_recent_log))

def filter_logs_by_date(logs,output_file="filtered_logs.txt"):
    start_date_input=input('enter start date ')
    end_date_input=input('enter end date ')
    try:
        start_date=datetime.strptime(start_date_input,"%Y-%m-%d").date()
        end_date=datetime.strptime(end_date_input,"%Y-%m-%d").date()
        filtered_logs=[]
        for log in logs:
            time_stamp=log[0]
            log_date=datetime.strptime(time_stamp,"%Y-%m-%d %H:%M:%S").date()
            if start_date<= log_date <=end_date:
                filtered_logs.append(log)
        with open(output_file,'w') as file:
            for log in filtered_logs:
                file.write(" ".join(log) + "\n")
    except:
        print('invalid date format')

temp_logs=test_file()
print(count_log_levels(temp_logs))
print(find_recent_log(temp_logs))
print(filter_logs_by_date(temp_logs))
