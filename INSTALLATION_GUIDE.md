# Установка на новой машине

Требования: Linux, Python 3.12, Git, curl. Для GPU-запуска — NVIDIA GPU и совместимый драйвер.

```bash
# Установить uv (если ещё не установлен)
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Скачать основной репозиторий
git clone https://github.com/gblssroman/hidden-messages-diffusion-agents-math.git
cd hidden-messages-diffusion-agents-math

# Скачать закреплённую версию dLLM и её evaluation harness
git clone https://github.com/ZHZisZZ/dllm.git code/third_party/dllm
git -C code/third_party/dllm checkout ca176752fbceec49c6b4777a2c18ae88e4eb10ed
git -C code/third_party/dllm submodule update --init lm-evaluation-harness

# Установить зависимости из uv.lock в локальную .venv
uv sync --locked

# Проверить импорты и доступность GPU
uv run --locked python -c "import torch, dllm, lm_eval, trl; print('Torch:', torch.__version__); print('CUDA:', torch.cuda.is_available()); print('Imports OK')"
```

Для GPU-запуска проверка должна показать `CUDA: True`.

## Вариант 1. VS Code / Cursor

Установить расширения **Python** и **Jupyter**. Открыть `.ipynb` → **Select Kernel → Python Environments** → выбрать `.venv/bin/python` из проекта.

## Вариант 2. JupyterLab в браузере

```bash
# Зарегистрировать kernel ноутбука
uv run --locked python -m ipykernel install --user \
  --name hidden-messages-math --display-name "hidden_messages_math"

# Запустить JupyterLab
uv run --locked jupyter lab
```

В браузере открыть адрес из терминала и выбрать kernel **hidden_messages_math** в ноутбуке.

Веса моделей скачиваются отдельно из ноутбука через Hugging Face.

В основной репозиторий должны быть закоммичены `pyproject.toml`, `uv.lock`, `.python-version` и `.gitignore`. Папка `code/third_party/dllm/` остаётся в `.gitignore`.
