import os
import time
import argparse
import vars

parser = argparse.ArgumentParser(description='git atuo committer')
parser.add_argument('--maker', action='store_true', dest='maker', default=False)
parser.add_argument('--viewer', action='store_true', dest='viewer', default=False)
args = parser.parse_args()

# Convert resolution
ww_res = ['1280', '1024']
os.chdir(vars.PROGRAM_LOCATION + '/QRes')
os.system(f'QRes.exe /x:{ww_res[0]} /y:{ww_res[1]}')

#launch Wonderware
os.chdir(vars.WW_PATH)
if args.viewer: os.startfile('view.exe')
if args.maker: os.startfile('wm.exe')
time.sleep(2)

# Restore resolution
os.chdir(vars.PROGRAM_LOCATION + '/QRes')
os.system(f'QRes.exe /x:{vars.ORIGINAL_RES[0]} /y:{vars.ORIGINAL_RES[1]}')