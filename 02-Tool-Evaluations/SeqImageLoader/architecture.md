# My Overview of ComfyUI-SeqImageLoader Architecture

> **Note:** I gathered the information in this document from the official [GitHub repository](https://github.com/bruefire/ComfyUI-SeqImageLoader). I have not practically tested these nodes myself.

I found that **ComfyUI-SeqImageLoader** operates as a frontend-backend extension, combining Python-based node logic with a JavaScript-based custom UI for the mask editor.

## Core Components

### 1. SequentialImageLoader Node
I observed that this node handles the loading of image sequences from a directory.
-   **Inputs:** Directory path, start index, end index.
-   **Outputs:** Batch of images, batch of masks, image count.
-   **Mechanism:** It reads files from the disk and pairs them with any masks created in the editor.

### 2. VideoFrameExtractor Node
I found this node extends the functionality to video files.
-   **Inputs:** Video file path (MP4).
-   **Mechanism:** It likely uses `ffmpeg` or a similar library (the docs mention `getVideoFrames.js`) to extract frames into a temporary directory, which are then treated similarly to the sequence loader.

### 3. Mask Editor GUI
I noted that the core interaction happens in a custom "MaskEditor" window.
-   **Features:** This interface provides canvas-based tools for drawing masks and sketches.
-   **Data Flow:** When the user saves edits in the GUI, the mask data is likely serialized and passed back to the Python backend to be output as mask tensors.

## Workflow Integration
I found that these nodes are designed to be the **entry point** for video or sequence editing workflows. They feed directly into inpainting nodes, AnimateDiff pipelines, or other image-to-image processes that require paired image and mask inputs.
