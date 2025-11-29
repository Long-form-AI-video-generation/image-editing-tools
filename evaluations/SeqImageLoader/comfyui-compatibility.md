# My Assessment of ComfyUI-SeqImageLoader Compatibility

> **Note:** I gathered the information in this document from the official [GitHub repository](https://github.com/bruefire/ComfyUI-SeqImageLoader). I have not practically tested these nodes myself.

## My Verdict: Fully Compatible
I found that **ComfyUI-SeqImageLoader** is a native ComfyUI extension. Therefore, it is fully compatible by design.

## Installation
I found that installation is straightforward:
1.  Clone the repository into the `custom_nodes` directory of your ComfyUI installation.
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/bruefire/ComfyUI-SeqImageLoader.git
    ```
2.  Restart ComfyUI.

## Usage
I discovered that using the tool involves a few specific steps:
1.  **Add Node:** Add either `SequentialImageLoader` or `VideoFrameExtractor` to your workflow.
2.  **Load Content:** Specify the directory or video file.
3.  **Open Editor:** Right-click the node and select **"Open In MaskEditor"**.
4.  **Edit:** Perform your masking and sketching in the popup window and click Save.
5.  **Connect:** Connect the `images` and `mask_images` outputs to your downstream nodes (e.g., VAE Encode, Set Latent Noise Mask).

## Requirements
I noted the following requirements:
-   **FFmpeg:** Likely required for the video extraction features.
-   **Browser:** A modern web browser to support the canvas-based Mask Editor.
-   **Disk Space:** The tool creates temporary frame data in an `input/` directory, which I noted should be cleaned up periodically.
