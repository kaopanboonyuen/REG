# Use a lightweight base with Python and CUDA support
FROM pytorch/pytorch:2.0.1-cuda11.8-cudnn8-runtime

WORKDIR /workspace

# Copy your project files
COPY . /workspace

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: show help or help instruction
CMD ["python", "src/train.py", "--help"]