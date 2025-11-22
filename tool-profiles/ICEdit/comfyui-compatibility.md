# ICEdit‑ComfyUI Official Workflow

This document evaluates ComfyUI compatibility with ICEdit by describing required nodes, installation steps, and usage guidance. It highlights which ComfyUI nodes ICEdit integrates with, known limitations, and recommended model and plugin configurations to ensure reliable operation.



## ComfyUI Workflow

- You can directly load images using the **DiptychCreate** node.
- Images processed by other ComfyUI nodes can also be used in this case, the DiptychCreate node’s loaded image is ignored.
- The DiptychCreate node must load an image to prevent workflow errors.


## Installation

### Prerequisites
Please first install ComfyUI with the following commands:
```bash
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
pip install -r requirements.txt
```

In addition, you need to install [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials) and [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use).


### Installation Methods
#### 1. ComfyUI-Manager Installation
1. Install [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) with the following commands:

```bash
   cd custom_nodes
   git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager
   ```
2. Launch ComfyUI:
```bash
   cd ..	# Make sure you are in the ComfyUI root directory
   python main.py
```


3. Open the ComfyUI Manager, select Install via Git URL, input the URL:
```bash
   https://github.com/hayd-zju/ICEdit-ComfyUI-official.git`
```
4. Then install it and just wait a minute.

#### 2. Manual Installation

1.  Clone this repository into the `custom_nodes` directory inside ComfyUI:
```bash
   cd custom_nodes
   git clone https://github.com/hayd-zju/ICEdit-ComfyUI-official.git
```
2. Launch ComfyUI:
```bash
   cd ..	# Make sure you are in the ComfyUI root directory
   python main.py
```
## Usage
1. Download Required Models: If you can connect to Huggingface, you don't need to download the weights. Otherwise, you need to download the weights to local.
    - [Flux.1-fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev).
    - [ICEdit-normal-LoRA](https://huggingface.co/RiverZ/normal-lora/tree/main).
    
2. Use  workflow example in [example_workflow](https://github.com/hayd-zju/ICEdit-ComfyUI-official/tree/main/example_workflow): You can directly drag the JSON file onto the ComfyUI interface.


