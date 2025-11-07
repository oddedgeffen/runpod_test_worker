import runpod

def handler(event):
    """Simple hello-world test."""
    return {"message": "RunPod worker is alive!"}

runpod.serverless.start({"handler": handler})
