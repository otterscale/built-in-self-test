import os
import subprocess
import sys

nfs_target = '/mnt/nfs/bist'
output_format = "json"

def fio(fio_config, target):
    fio_cmd = ["fio", "--filename", target, "--name", target , "--output-format", output_format]
    for key, value in fio_config.items():
        param = "--" + key
        if value in ('True'):
            fio_cmd.append(param)
        else:
            fio_cmd.append(param)
            fio_cmd.append(value)

    try:
        subprocess.check_call(fio_cmd)
        #print(f"Fio start {target}")
    except subprocess.CalledProcessError as e:
        print(f"Fio failed: {e}")
        sys.exit(1)

def run(fio_config, target, is_nfs=False):
    if is_nfs:
        fio(fio_config, nfs_target)
    else:
        fio(fio_config, target)