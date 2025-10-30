# Face Swap Backend

Face swapping API using InsightFace and Gradio, deployed on Render.

## API Endpoint

Once deployed, the API will be available at:

## Usage

Use the Gradio API format:
1. POST to `/upload` to upload files
2. POST to `/call/swap_face` to start processing
3. GET from `/call/swap_face/{event_id}` to get results

## Local Development

```bash
pip install -r requirements.txt
python app.py
