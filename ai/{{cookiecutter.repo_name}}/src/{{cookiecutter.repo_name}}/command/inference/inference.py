import requests
import json


def submit_inference(args):
    host = "localhost"
    if args.server:
        host = args.server

    port = "3000"
    if args.port:
        port = args.port

    inference_request = ""
    if args.json:
        inference_request = json.loads(args.json)

    url = f"http://{host}:{port}/ai/{{cookiecutter.model_name}}/inference"

    resp = requests.post(
            url,
            json=inference_request
        )

    if resp.status_code == 200:
        resp_json = resp.json()
        print(resp_json["prediction"])
    else:
        print("ERROR!")
