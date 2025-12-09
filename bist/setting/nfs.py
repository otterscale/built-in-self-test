import os
import subprocess
import sys

mount_point ='/mnt/nfs'


def mount_nfs(nfs_endpoint, path, mount_point):
    mount_nfs_cmd = ["mount", "-t", "nfs4", f"{nfs_endpoint}:{path}", mount_point]
    try:
        subprocess.check_call(mount_nfs_cmd)
        #print(f"Mount successfully：{nfs_endpoint}:{path} -> {mount_point}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Mount failed: {e}")
        sys.exit(1)
        return False


def initialize(nfs_config):
    return mount_nfs(nfs_config['endpoint'] , nfs_config['path'], mount_point)


def cleanup():
    umount_nfs_cmd = ["umount", mount_point]
    try:
        subprocess.check_call(umount_nfs_cmd)
        #print(f"Umount successfully： {mount_point}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Umount failed: {e}")
        sys.exit(1)
        return False