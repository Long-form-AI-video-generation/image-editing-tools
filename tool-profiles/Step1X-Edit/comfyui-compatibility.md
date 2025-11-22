# ComfyUI Compatibility — Step1X-Edit Integration

This document describes how the `ComfyUI_Step1X-Edit` extension integrates the **Step1X-Edit** model into ComfyUI, installation steps, usage, and important compatibility considerations.

---

## 1. Overview

- The `raykindle/ComfyUI_Step1X-Edit` repository provides a **custom node extension** for ComfyUI, enabling the use of Step1X-Edit’s instruction-based image editing. 
- It supports **FP8 quantized inference**, **Flash-Attention** acceleration, and **TeaCache** acceleration for faster inference with minimal quality loss. 
- This makes Step1X-Edit more accessible for high-performance image editing within ComfyUI workflows. 

---

## 2. Installation

1. **Clone the Extension**

   Clone the `ComfyUI_Step1X-Edit` repository into your ComfyUI custom nodes folder:

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/raykindle/ComfyUI_Step1X-Edit.git
   ```
2. **Install the required dependencies:**

   Step 1: Install ComfyUI_Step1X-Edit dependencies
   ```bash
      cd ComfyUI_Step1X-Edit
      pip install -r requirements.txt
   ```

   Step 2: Install [flash-attn](https://github.com/Dao-AILab/flash-attention), here we provide a script to help find the pre-built wheel suitable for your system.
   ```bash
   python utils/get_flash_attn.py
   ```

   The script will generate a wheel name like flash_attn-2.7.2.post1+cu12torch2.5cxx11abiFALSE-cp310-cp310-linux_x86_64.whl, which could be found in:

    - Linux version: [Dao-AILab's flash-attn releases](https://github.com/Dao-AILab/flash-attention/releases)
    - Windows version: [kingbri1's flash-attn releases](https://github.com/kingbri1/flash-attention/releases)

   Then you can download the corresponding pre-built wheel and install it following the instructions in [flash-attn](https://github.com/Dao-AILab/flash-attention).

   Note: Even if the CUDA and Torch versions don't match exactly, you can still successfully install flash-attention. However, for optimal performance and compatibility, it's recommended to use versions that match your system exactly.

   Step 3: Download Step1X-Edit-FP8 model
   ```bash
   ComfyUI/
    └── models/
    ├── diffusion_models/
    │   └── step1x-edit-i1258-FP8.safetensors
    ├── vae/
    │   └── vae.safetensors
    └── text_encoders/
        └── Qwen2.5-VL-7B-Instruct/
   ```


   - Step1X-Edit diffusion model: Download `step1x-edit-i1258-FP8.safetensors` from [HuggingFace](https://huggingface.co/meimeilook/Step1X-Edit-FP8/tree/main) and place it in ComfyUI's models/diffusion_models directory
   - Step1X-Edit VAE: Download  `vae.safetensors` from [HuggingFace](https://huggingface.co/meimeilook/Step1X-Edit-FP8/tree/main) and place it in ComfyUI's models/vae directory
   - Qwen2.5-VL model: Download [Qwen2.5-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct/tree/main) and place it in ComfyUI's `models/text_encoders/Qwen2.5-VL-7B-Instruct` directory


##  Usage

1. Launch **ComfyUI**.
2. Create a **new workflow**.
3. Add:
   - **Step1X-Edit Model Loader**  
     or  
   - **Step1X-Edit TeaCache Model Loader** (⚡ ~2× speed)
4. Configure model settings:
   - `diffusion_model` → `step1x-edit-i1258-FP8.safetensors`
   - `vae` → `vae.safetensors`
   - `text_encoder` → `Qwen2.5-VL-7B-Instruct`
   - Set optional parameters (`dtype`, `quantized`, `offload`)
   - For TeaCache: set `teacache_threshold`
5. Add a **Step1X-Edit Generate** node  
   or  
   **Step1X-Edit TeaCache Generate** (if using TeaCache)
6. Provide:
   - an **input image**
   - an **editing prompt**
7. Run the workflow and get edited images.

---

##  Parameters

### **Step1X-Edit Model Loader**

| Parameter | Description |
|----------|-------------|
| `diffusion_model` | Select the Step1X-Edit `.safetensors` diffusion model |
| `vae` | Select the Step1X-Edit VAE file |
| `text_encoder` | Path name of Qwen2.5-VL model folder |
| `dtype` | Precision (`bfloat16`, `float16`, `float32`) |
| `quantized` | Use FP8 quantized weights (recommended: `true`) |
| `offload` | Offload models to CPU when idle |

---

### **Step1X-Edit TeaCache Model Loader — Additional Parameters**

| Parameter | Description |
|-----------|-------------|
| `teacache_threshold` | Controls speed–quality tradeoff |
| `verbose` | Print TeaCache debug logs |

**Recommended TeaCache Thresholds**

| Threshold | Speedup |
|-----------|---------|
| `0.25` | ~1.5× |
| `0.4` | ~1.8× |
| `0.6` | **2× (recommended)** |
| `0.8` | ~2.25× with minor quality loss |

---

##  Step1X-Edit Generate / TeaCache Generate

| Parameter | Description |
|-----------|-------------|
| `model` | Loaded Step1X-Edit model bundle |
| `image` | Input image to edit |
| `prompt` | Instruction describing desired edit |
| `negative_prompt` | What to avoid |
| `steps` | Number of denoising steps |
| `cfg_scale` | Guidance scale |
| `image_size` | Output size (512 recommended) |
| `seed` | Random seed for reproducibility |

---

## ⚡ TeaCache Acceleration

TeaCache brings major performance boosts:

- Up to **2× faster inference**
- No fine-tuning required (training-free)
- Adaptive feature caching based on timestep embeddings
- Adjustable speed–quality tradeoff via threshold
- Minimal memory overhead


## 🧠 Memory Requirements

The **Step1X-Edit** model requires significant GPU memory for inference.  
Benchmark below is measured at **768px resolution** with **10 sampling steps**.

### Performance & VRAM Usage

| Model Version | Peak GPU Memory | Native Speed | ~1.5× Speedup (threshold = 0.25) | ~2.0× Speedup (threshold = 0.6) |
|---------------|------------------|--------------|----------------------------------|---------------------------------|
| **Step1X-Edit-FP8 (offload = False)** | **31.5 GB** | 17.4 s | 11.2 s | **7.8 s** |

> **Note:** Tests were performed on a single **H20 GPU**.

---

### 🔽 Reducing VRAM Usage

To run the model on GPUs with less memory, enable:

- **`quantized = true`** — uses FP8 optimization  
- **`offload = true`** — moves inactive layers to CPU to save VRAM  

Both options are available in the **Step1X-Edit Model Loader** node inside ComfyUI.

---

