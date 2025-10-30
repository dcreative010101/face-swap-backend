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


---

### **Step 4: Deploy to Render**

1. Go to https://render.com
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect GitHub"** (authorize if needed)
4. Select your **`face-swap-backend`** repository
5. Render will auto-detect the `render.yaml`
6. Click **"Create Web Service"**
7. Wait ~10 minutes for first deploy

You'll get a URL like: `https://face-swap-backend-abc123.onrender.com`

---

### **Step 5: Update Your Next.js [`route.ts`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FKuting%2FVScode%20Projects%2FMy%20Project%2FProject%202%2Fface-swap%2Fapp%2Fapi%2Fface-swap%2Froute.ts%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "d:\Kuting\VScode Projects\My Project\Project 2\face-swap\app\api\face-swap\route.ts")**

```typescript
// Just change this ONE line at the top of your existing route.ts:
const BACKEND_URL = "https://face-swap-backend-abc123.onrender.com"; // Your Render URL

// Then update all fetch URLs:
await fetch(`${BACKEND_URL}/upload`, {
  // ... rest stays the same
});

┌─────────────────────────┐
│   GitHub Repository     │
│  "face-swap-backend"    │
│  ├── app.py            │
│  ├── requirements.txt  │
│  └── render.yaml       │
└─────────────────────────┘
           │
           │ Connected to
           ▼
┌─────────────────────────┐
│      Render.com         │
│   (Auto-deploys)        │
│  https://your-app.      │
│    onrender.com         │
└─────────────────────────┘
           │
           │ Called by
           ▼
┌─────────────────────────┐
│   Your Next.js App      │
│  (app/api/face-swap/    │
│     route.ts)           │
└─────────────────────────┘
