# SHMT on RunPod (Serverless)

This repo contains a minimal, production-ready setup to deploy SHMT (Self-supervised Hierarchical Makeup Transfer) on RunPod Serverless, with Docker + GitHub Actions.

## Contents
- `shmt-runpod/`: Dockerized RunPod serverless worker (CUDA base, SHMT checkout, handler)
- `.github/workflows/deploy-runpod.yml`: Builds and pushes Docker image to Docker Hub and updates the RunPod Template image

## Weights (H0, H4, VQ-f4)
Weights are downloaded automatically at cold start using env vars:
- `MAKEUP_SHMT_H0_ID` (default: `1zed2At-qnIOXewkZsGq8GODEIxmaxMAE`)
- `MAKEUP_SHMT_H4_ID` (default: `19Kt-5wgqyLty_v8G-oez8COjDqEcApDF`)
- `MAKEUP_SHMT_VQF4_URL` (default: `https://ommer-lab.com/files/latent-diffusion/vq-f4.zip`)

If you prefer not to download on start:
- Option A (recommended): Upload weights to a RunPod Volume and mount it to `/workspace/models`
- Option B: Bake weights into the image (add RUN wget/curl lines in `Dockerfile`). This increases image size significantly.

## Deploy via GitHub Actions (Docker Hub)
1) Create a new GitHub repo and push this folder.
2) Add repo secrets:
   - `DOCKER_USERNAME`
   - `DOCKER_PASSWORD`
   - `RUNPOD_API_KEY`
   - (one of) `RUNPOD_ENDPOINT_ID` or `RUNPOD_ENDPOINT_NAME`
3) Push to `master`/`main` → Action builds and pushes image → updates the RunPod Template image.

## RunPod Endpoint Env Vars
Set on the endpoint:
- `MAKEUP_SHMT_H0_ID`, `MAKEUP_SHMT_H4_ID`, `MAKEUP_SHMT_VQF4_URL` (overwrite if you host your own)

## Test Request
Use the RunPod Serverless invoke URL for your endpoint:

```bash
curl -s -X POST "https://api.runpod.io/v2/<ENDPOINT_ID>/run" \
  -H "Authorization: Bearer <RUNPOD_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "source_url": "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=400",
      "reference_url": "https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=400",
      "ddim_steps": 50,
      "guidance_scale": 1.0
    }
  }'
```

## Local build (optional)
From repo root:
- `docker build -t <user>/shmt-runpod:dev shmt-runpod`
- `docker run --rm -it <user>/shmt-runpod:dev`

