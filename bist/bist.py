#!/usr/bin/python3
import os
import subprocess

from setting import nfs, block, s3
from benchmark import fio, warp

base_benchmark = {'rbd': False, 'rados': False}

nfs_config = {}
fio_config = {}
block_config = {}
warp_config = {}


def main():
    benchmark_type = os.environ.get('BENCHMARK_TYPE')
    for key, value in os.environ.items():
        if key.startswith("BENCHMARK_ARGS_NFS_"):
            nfs_config.update({key[len("BENCHMARK_ARGS_NFS_"):].lower(): value})
        elif key.startswith("BENCHMARK_ARGS_FIO_"):
            fio_config.update({key[len("BENCHMARK_ARGS_FIO_"):].lower(): value})
        elif key.startswith("BENCHMARK_ARGS_BLOCK_"):
            block_config.update({key[len("BENCHMARK_ARGS_BLOCK_"):].lower(): value})
        elif key.startswith("BENCHMARK_ARGS_WARP_"):
            warp_config.update({key[len("BENCHMARK_ARGS_WARP_"):].lower(): value})

    if benchmark_type == 'nfs':
        if nfs.initialize(nfs_config):
            fio.run(fio_config, target="", is_nfs=True)
            nfs.cleanup()
    elif benchmark_type == 'block':
        block_target = block.initialize(block_config)
        if block_target:
            fio.run(fio_config, block_target, is_nfs=False)
            block.cleanup(block_config)
    elif benchmark_type == 's3':
        if s3.initialize(warp_config):
            warp.run(warp_config)


if __name__ == '__main__':
    main()