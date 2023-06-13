import beam

app = beam.App(
    name="mpt-7b-chat",
    cpu=8,
    memory="64Gi",
    gpu="A10G",
    python_version="python3.8",
    python_packages=["transformers", "torch", "numpy", "einops", "langchain"],
    commands=["apt-get update && apt-get install -y ffmpeg"]
)

app.Mount.PersistentVolume(path="./models", name="models")

# The REST API trigger exposes the app as a REST endpoint when deployed
app.Trigger.RestAPI(
    inputs={"query": beam.Types.String()},
    outputs={"pred": beam.Types.Json()},
    handler="run.py:start_conversation",
)
