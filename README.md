# supermicro-gpu-fan-controller
Fan controller for "passive" cooled NVIDIA GPUs via `ipmitool` and `nvidia-smi`.

🚧 _This project is under development, and not ready for use._ 🚧

## Why?
- If you plan to build a home lab system using used parts, you may encounter suboptimal situations. For example, in my case, I have a passive-cooled NVIDIA GPU that was extracted from a server system. While it is a great GPU, it is not specifically designed for use in a desktop tower-like system.
- Although a fan can be attached to the GPU, it lacks the ability to determine the GPU's temperature, making it unable to provide appropriate cooling. This becomes particularly important when you seek a balance between noise and performance.

## How?
- This project uses `ipmitool` to control the fan speed of the system. It also uses `nvidia-smi` to determine the temperature of the GPU.

## Requirements
- Linux (mainly targeting Ubuntu 22.04)
- `ipmitool`
- `nvidia-smi`
- `python3.10+`

## Installation
TODO

## Usage
TODO

## Acknowledgements / References
- [petersulyok/smfc](https://github.com/petersulyok/smfc)
- [skokec/superfans-gpu-controller](https://github.com/skokec/superfans-gpu-controller)

