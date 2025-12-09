import os
import subprocess
import sys


def warp(warp_config):
    warp_cmd = ["warp", "--json", "--full"]
    for key, value in warp_config.items():
        param = "--" + key.replace("_", "-")
        if value in ('delete', 'get', 'list', 'mixed', 'multipart', 'put', 'stat', 'versioned', 'zip'):
            warp_cmd.insert(1, value)
        elif value in ('True'):
                warp_cmd.append(param)
        else:
            warp_cmd.append(param)
            warp_cmd.append(value)

    try:
        subprocess.check_call(warp_cmd)
        #print(f"warp start")
    except subprocess.CalledProcessError as e:
        print(f"warp failed: {e}")
        sys.exit(1)


def run(warp_config):
    warp(warp_config)