import os
import subprocess
import sys
import time


def map_image(pool, image):
    status_image_cmd = ["rbd", "status", f"{pool}/{image}"]
    map_image_cmd = ["rbd", "map", "-o", "noudev", f"{pool}/{image}"]
    try:
        #subprocess.check_call(map_image_cmd, stdout=subprocess.DEVNULL)
        while "none" not in subprocess.check_output(status_image_cmd, text=True).strip().lower():
            time.sleep(5)

        block_target = subprocess.check_output(map_image_cmd, text=True).strip()
        return block_target
    except subprocess.CalledProcessError as e:
        print(f"Map failed: {e}")
        sys.exit(1)
        return False


def initialize(block_config):
    return map_image(block_config['pool'] , block_config['image'])


def cleanup(block_config):
    pool = block_config['pool']
    image = block_config['image']
    unmap_image_cmd = ["rbd", "unmap", "-o", "noudev", f"{pool}/{image}"]
    try:
        subprocess.check_call(unmap_image_cmd, stdout=subprocess.DEVNULL)
        #print(f"Unmap successfully： {pool}/{image}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Unmap failed: {e}")
        sys.exit(1)
        return False