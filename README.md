## mosaicml/mpt-7b-chat

This code demonstrates how to run the [mosaicml/mpt-7b-chat](https://huggingface.co/mosaicml/mpt-7b-chat) model

## Deploying on Beam

You can easily deploy the code as web endpoints:

1. Create an account on [Beam](https://beam.cloud)
2. Download the CLI and Python-SDK. [Instructions here](https://docs.beam.cloud/getting-started/quickstart).
3. run `beam deploy app.py` from the working directory.

## Example Request

```cURL
 curl -X POST --compressed "https://beam.slai.io/cjm9u" \
   -H 'Authorization: Basic [ADD_YOUR_AUTH_TOKEN]' \
   -H 'Content-Type: application/json' \
   -d '{"query": "What is up?"}'
```

## Example Response

```cURL
{"pred":{"output_text":" I'm good and you?"}}
```
