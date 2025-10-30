import os
import sys
import tempfile
from pathlib import Path

print("=" * 60)
print("FACE-SWAP BACKEND (Render Deployment)")
print("=" * 60)

# Import packages
try:
    import numpy as np
    from PIL import Image
    import cv2
    import onnxruntime as ort
    import insightface
    from insightface.app import FaceAnalysis
    import gradio as gr
    print("All imports successful")
except ImportError as e:
    print(f"Import failed: {e}")
    sys.exit(1)

# Initialize face analyzer
print("🔧 Initializing face analyzer...")
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, det_size=(640, 640))
print("Face analyzer ready\n")

def swap_face(source_img, target_img, use_enhancer=False):
    """
    Swap faces between source and target images.
    """
    print(f"\nStarting face swap (enhancer: {use_enhancer})")
    
    if source_img is None or target_img is None:
        print("Missing input images")
        return None
    
    try:
        # Convert to BGR
        source_bgr = cv2.cvtColor(source_img, cv2.COLOR_RGB2BGR)
        target_bgr = cv2.cvtColor(target_img, cv2.COLOR_RGB2BGR)
        
        # Detect faces
        source_faces = app.get(source_bgr)
        if len(source_faces) == 0:
            print("No face in source")
            return None
        
        target_faces = app.get(target_bgr)
        if len(target_faces) == 0:
            print("No face in target")
            return None
        
        print(f"Found {len(source_faces)} source face(s), {len(target_faces)} target face(s)")
        
        # Swap face
        result_bgr = target_bgr.copy()
        source_face = source_faces[0]
        
        for target_face in target_faces:
            bbox = target_face.bbox.astype(int)
            x1, y1, x2, y2 = bbox
            
            h, w = result_bgr.shape[:2]
            x1, y1 = max(0, x1), max(0, y1)
            x2, y2 = min(w, x2), min(h, y2)
            
            source_bbox = source_face.bbox.astype(int)
            sx1, sy1, sx2, sy2 = source_bbox
            source_region = source_bgr[sy1:sy2, sx1:sx2]
            
            if source_region.size == 0:
                continue
            
            target_size = (x2 - x1, y2 - y1)
            if target_size[0] > 0 and target_size[1] > 0:
                resized = cv2.resize(source_region, target_size)
                result_bgr[y1:y2, x1:x2] = resized
        
        result_rgb = cv2.cvtColor(result_bgr, cv2.COLOR_BGR2RGB)
        print("Face swap complete\n")
        return result_rgb
        
    except Exception as e:
        print(f"Error: {e}\n")
        return None

# Create Gradio interface
demo = gr.Interface(
    fn=swap_face,
    inputs=[
        gr.Image(label="Source Face", type="numpy"),
        gr.Image(label="Target Image", type="numpy"),
        gr.Checkbox(label="Use Enhancer", value=False)
    ],
    outputs=gr.Image(label="Result", type="numpy"),
    title="Face Swap API",
    description="Face swapping service deployed on Render",
    allow_flagging="never",
    api_name="swap_face"
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    print(f"\nLaunching on port {port}...")
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        show_error=True
    )
