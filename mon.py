import subprocess, time

# --------------------------------------------------------------------- #
# get_cpuload
localtime = time.gmtime()
log_path_load_avg = '/home/centos/sa/logs/'
log_file_load_avg = str(time.strftime('%m_%d_%y',localtime))
log_path_load_avg += 'load_avg_' + log_file_load_avg + '.log'

log_path_script = '/home/centos/sa/logs/script.log'

log_time = str(time.strftime('%H:%M:%S %m %d %y',localtime)) 

def get_cpuload():
    # cmd = "uptime | grep -ohe '[s:][ ].*' | awk '{ print \"1m: \"$2 \" 5m: \"$3 \" 15m: \" $4}'"
    cmd = 'uptime'

    process_tmp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        _, _, current_users,  one_m, five_m, fifteen_m = str(output.rstrip('\n'.encode())).lstrip("b'").rstrip("'").split(',')
        
        current_users = current_users.rstrip('users').replace(' ', '')
        one_m = one_m.lstrip('load average:').replace(' ', '')
        five_m = five_m.replace(' ', '')
        fifteen_m = fifteen_m.replace(' ', '')

        with open (log_path_load_avg,'a') as f:
            f.write(log_time + ' ' + one_m + ' ' + five_m + ' ' + fifteen_m + '\n')

        return  current_users,  one_m, five_m, fifteen_m

    else:
        with open (log_path_load_avg,'a') as f:
            f.write(log_time + 'ERROR' + '\n')

        return "ERROR"
# --------------------------------------------------------------------- #
if get_cpuload() != 'ERROR':
     with open (log_path_script,'a') as f:
            f.write(log_time + ' Success' + '\n')
else:
    with open (log_path_script,'a') as f:
        f.write(log_time + ' Error' + '\n')