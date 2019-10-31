#WARNING: Python 3.7 or later needed!
import os
import asyncio
import sys
import time

async def kill(tar,server):
    if tar.strip()=='shutdown':
        os.system(f'start shutdown -s -m \\\\{server.strip()} -t 00')
    else:
        print(f'@taskkill /S {server.strip()} /IM {tar.strip()} /F')
        os.system(f'start taskkill /S {server.strip()} /IM {tar.strip()} /F')
async def count_time_do(*args,**kwargs):
    kill_task=asyncio.create_task(kill(*args,**kwargs))
    try:
        await asyncio.wait_for(kill_task,timeout=PROCESS_TIMEOUT)
    except asyncio.TimeoutError:
        return False
    else:
        return True
async def main(times,task,cpt_list):
    task_list=[]
    for cpt in cpt_list:
        task_list.append(asyncio.create_task(count_time_do(task,cpt)))
    result=await asyncio.gather(*task_list)
    fail,success=0,0
    for each in result:
        if each==False:
            fail+=1
        else:
            success+=1
    print('-'*20)
    print(f'{success} success(es), {fail} timeout(s)')
    
PROCESS_TIMEOUT=5
if len(sys.argv)!=2:
    raise SyntaxError('Invalid arguments.')
else:
    filename=sys.argv[1]
    config=open(filename).readlines()
print('PlKiller Ultimate-rc2[Author:President Bridgman]')
print('-'*20)
times=config[0]
task=config[1]
cpt_list=config[2:]
asyncio.run(main(times,task,cpt_list))
