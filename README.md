# Lip Sync Project

This project provides a lip-syncing solution using Python. Follow the steps below to set up the environment and run the project.

## Prerequisites

- Ensure you have Python 3.8 or higher installed.
- CUDA is required for this project. The higher the CUDA version, the better. You can check your CUDA version using the following command:
    ```bash
    nvcc --version
    ```

## Installation

1. **Install Poetry**  
     If you don't have Poetry installed, you can install it using the following command:
     ```bash
     curl -sSL https://install.python-poetry.org | python3 -
     ```

2. **Set Up the Poetry Environment**  
     Navigate to the project directory and install dependencies without updating the `pyproject.toml` versions:
     ```bash
     poetry install --no-root
     ```

3. **Activate the Poetry Environment**  
     Enter the Poetry environment:
     ```bash
     poetry shell
     ```
4. **Verify PyTorch and CUDA Compatibility**  
    After activating the environment, check the versions of `torch`, `torchaudio`, and `torchvision` to ensure they are compatible with CUDA. Run the following commands to verify:
    ```bash
    poetry run python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
    poetry run python -c "import torchaudio; print(torchaudio.__version__)"
    poetry run python -c "import torchvision; print(torchvision.__version__)"
    ```
    The output should display the library versions along with the CUDA version in the format `<version>+cu<cuda_version>`. For example:
    ```
    2.6.0+cu124
    0.21.0+cu124
    2.6.0+cu124
    ```
    If the versions are not compatible with CUDA, you can install the appropriate versions by visiting the official PyTorch website for the most up-to-date installation instructions and compatible versions: [PyTorch Get Started Locally](https://pytorch.org/get-started/locally/). Replace the versions in the command below with those suitable for your CUDA setup:

    ```bash
    poetry run pip install torch==<torch_version>+<cuda_version> torchvision==<torchvision_version>+<cuda_version> torchaudio==<torchaudio_version>+<cuda_version> -f https://download.pytorch.org/whl/torch_stable.html
    ```
5. **Download Required Models**  
     Run the following script to download the necessary models:
     ```bash
     rm -rf SadTalker/checkpoints
     bash SadTalker/scripts/download_models.sh
     ```

## Running the Project

To execute the lip-syncing script, use the following command:
```bash
poetry run python lip_sync/lipsync.py
```

## Notes

- Ensure your system has a compatible GPU with CUDA installed.
- For more details, refer to the project documentation or contact the maintainers.
