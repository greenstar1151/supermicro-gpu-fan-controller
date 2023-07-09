from __future__ import annotations

import subprocess
from dataclasses import dataclass


@dataclass(slots=True)
class GPUInfo:
    index: int
    name: str
    temperature: int
    utilization: int


def get_gpu_info() -> list[GPUInfo]:
    """
    Get GPU information using nvidia-smi.

    Returns:
        list[GPUInfo]: List of GPU information.
    """
    cmd = [
        "nvidia-smi",
        "--query-gpu=index,name,temperature.gpu,utilization.gpu",
        "--format=csv,noheader,nounits"
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")

    if result.returncode != 0:
        raise RuntimeError("Failed to get GPU information.")

    gpu_info_list: list[GPUInfo] = []
    for line in result.stdout.splitlines():
        index, name, temperature, utilization = map(str.strip, line.split(","))
        gpu_info_list.append(GPUInfo(int(index), name, int(temperature), int(utilization)))

    return gpu_info_list
