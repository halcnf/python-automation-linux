import subprocess, time

# --------------------------------------------------------------------- #
# get_cpuload

def get_cpuload():
    # cmd = "uptime | grep -ohe '[s:][ ].*' | awk '{ print \"1m: \"$2 \" 5m: \"$3 \" 15m: \" $4}'"
    cmd = "uptime"
    

    process_tmp = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, err) = process_tmp.communicate()
    p_status = process_tmp.wait()

    if p_status == 0:
        _, _, current_users,  one_m, five_m, fifteen_m = str(output.rstrip('\n'.encode())).lstrip("b'").rstrip("'").split(',')
        
        current_users = current_users.rstrip('users').replace(' ', '')
        one_m = one_m.lstrip('load average:').replace(' ', '')
        five_m = five_m.replace(' ', '')
        fifteen_m = fifteen_m.replace(' ', '')

        with open ('logs/load_avg.log','a') as f:
            f.write(time.ctime() + ' ' + one_m + ' ' + five_m + ' ' + fifteen_m + '\n')

        return  current_users,  one_m, five_m, fifteen_m

    else:
        with open ('logs/load_avg.log','a') as f:
            f.write(time.ctime() + 'ERROR' + '\n')

        return "ERROR"
# --------------------------------------------------------------------- #
if get_cpuload() != 'ERROR':
     with open ('logs/script.log','a') as f:
            f.write(time.ctime() + ' Success' + '\n')
else:
    with open ('logs/script.log','a') as f:
        f.write(time.ctime() + ' Error' + '\n')