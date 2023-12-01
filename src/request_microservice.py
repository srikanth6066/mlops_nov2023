import requests
import os
from get_data import read_params
import argparse 

def request_response(config_path):
    config = read_params(config_path)
    url = config["url"]
    json_params = config["json_obj"]
    responses = requests.post(url, json = json_params)
    print(responses.text)


if __name__ == "__main__" :
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()

    request_response(config_path=parsed_args.config)