"""Run: uv run math_research/env_check.py."""

import sys
from importlib import import_module
from importlib.metadata import version

import torch

print("Python:", sys.version.split()[0])
print("Torch:", torch.__version__)
for package in ("dllm", "lm_eval", "transformers", "trl"):
    import_module(package)
    print(f"{package}: {version(package)}")

print("CUDA:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("BF16:", torch.cuda.is_bf16_supported())
