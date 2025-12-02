# My Overview of ComfyUI-ImageMagick Architecture

> **Note:** I gathered the information in this document from the official [GitHub repository](https://github.com/jtydhr88/ComfyUI-ImageMagick). I have not practically tested these nodes myself.

I found that **ComfyUI-ImageMagick** has a straightforward architecture that acts as a bridge between ComfyUI's tensor-based image format and the system-level `magick` executable.

## Core Components

### 1. The ImageMagick Node
I observed that the extension implements a single, versatile custom node named `ImageMagick`.
-   **Inputs:** It accepts up to 3 images (`image1`, `image2`, `image3`).
-   **Parameters:** It accepts up to 6 string parameters (`param1`...`param6`) which are passed as arguments to the command.
-   **Execution:**
    1.  I assume it saves the input ComfyUI images to temporary files.
    2.  It constructs a shell command using the `magick` executable and the provided parameters.
    3.  It executes the command.
    4.  It loads the resulting output image back into ComfyUI.

### 2. System Dependency
I noted that unlike many Python-only nodes, this extension **strictly requires** the ImageMagick software (version 7.x) to be installed on the host system and accessible via the system `PATH`.

## Workflow Integration
I found that this node is typically used as a **post-processing step**.
-   **Example Flow:** Generation -> VAE Decode -> ImageMagick (Threshold/Transparency) -> Save Image.
-   **Data Flow:** It handles the conversion between ComfyUI's internal format and standard image formats (PNG/JPG) required by the CLI tool transparently.
