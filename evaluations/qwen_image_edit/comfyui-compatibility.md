# My Assessment of Qwen-Image-Edit Compatibility

## My Verdict: Natively Supported in ComfyUI
I found that **Qwen-Image-Edit** is supported as a **native ComfyUI workflow** via Comfy-Org's official model packaging, meaning it does not require third-party custom nodes to run. The required nodes are built into recent ComfyUI versions.

## Installation

### ComfyUI Version Requirement
I found that you must be on the **latest ComfyUI (Nightly) version** for all nodes to be available. The Desktop version follows the stable release channel and may lag behind.

### Model Download
I discovered that Comfy-Org provides pre-packaged, quantized model files optimized for ComfyUI. The files should be placed in the following directory structure:

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_fp8_e4m3fn.safetensors
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

All model files are available at [Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI) and [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI) on Hugging Face.

## Usage

### Workflow Templates
I found that the official ComfyUI documentation provides ready-to-use JSON workflow files accessible directly from the **Workflow Templates** panel inside ComfyUI. For portable/self-deployed users, the workflow can also be loaded by dragging the PNG workflow image into ComfyUI or by downloading the JSON directly

### Node Loading Steps
I discovered the following node setup is required to complete the workflow:
1.  **Load Diffusion Model** → `qwen_image_edit_fp8_e4m3fn.safetensors`
2.  **Load CLIP** → `qwen_2.5_vl_7b_fp8_scaled.safetensors`
3.  **Load VAE** → `qwen_image_vae.safetensors`
4.  (Optional) **LoRA Loader** → `Qwen-Image-Lightning-4steps-V1.0.safetensors` for 4-step fast inference

### Speed Optimization
I noted that the **Qwen-Image-Lightning LoRA** (developed by LightX2V) is available as an optional drop-in for faster inference, reducing the number of diffusion steps to 4 and reportedly achieving significant speed gains. Enable the `LoraLoaderModelOnly` node in the workflow and use the KSampler settings noted in the workflow comments.

## Requirements
I noted the following prerequisites:
-   A working **ComfyUI installation** (latest Nightly recommended).
-   Sufficient **VRAM**: The model is 20B parameters. The FP8-quantized version provided by Comfy-Org significantly reduces memory requirements, but a high-VRAM GPU is still recommended (24GB+ for comfortable use).
-   The model is licensed under **Apache 2.0**, allowing commercial use.