# supermicro-gpu-fan-controller
Fan controller for "passive" cooled NVIDIA GPUs via `ipmitool` and `nvidia-smi`.

🚧 _This project is under development, and not ready for use._ 🚧

## Why?
- If you plan to build a home lab system using used parts, you may encounter suboptimal situations. For example, in my case, I have a passive-cooled NVIDIA GPU that was extracted from a server system. While it is a great GPU, it is not specifically designed for use in a desktop tower-like system.
- Although a fan can be attached to the GPU, it lacks the ability to determine the GPU's temperature, making it unable to provide appropriate cooling. This becomes particularly important when you seek a balance between noise and performance.

## Requirements
- Linux (mainly targeting Ubuntu 22.04)
- Working `ipmitool` (loaded with appropriate kernel modules)
- `nvidia-smi`
- `python3.10+`

## How?
- This project uses `ipmitool` to control the fan speed of the system. It also uses `nvidia-smi` to determine the temperature of the GPU.
- Since the Supermicro board features two "zones" for fan control, it is essential to connect the GPU fan to a separate zone from the one where the CPU fan is connected. Further details can be found in [this](https://forums.servethehome.com/index.php?resources/supermicro-x9-x10-x11-fan-speed-control.20/) article by PigLover.

## Current Strategy for Fan Control
- Connect the GPU fan to the Peripheral zone fan headers (e.g., FANA, FANB, etc.).
- Set the Fan Mode to "Optimal" to make Peripheral zone to prevent it from being overridden by automatic control, while allowing the CPU zone to be controlled automatically by BMC.

## Installation
TODO

## Usage
TODO

## Acknowledgements / References
- [petersulyok/smfc](https://github.com/petersulyok/smfc)
- [skokec/superfans-gpu-controller](https://github.com/skokec/superfans-gpu-controller)

