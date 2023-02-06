import json
import os
from pathlib import Path
import fcntl
from utils.rapper_function import func_loger

BASE_PATH = Path.cwd().joinpath('data')
ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))


@func_loger
def load_files(data_file: str):
    """
    Get file path from data folder
    :param data_file: File name without the .json
    :return: Returns file path
    """
    data_folder = {}
    try:
        with open(os.path.join(ROOT_DIR, f"data/{data_file}.json"), encoding="utf-8") as json_data:
            data_folder[f'{data_file}'] = json.load(json_data)
    except IOError as error:
        return error
    return data_folder[f"{data_file}"]


@func_loger
def write_files(payload: object, data_file: str):
    """
    Writes to a Json file
    :param payload: Json payload
    :param data_file: File name without the .json
    """
    try:
        with open(os.path.join(ROOT_DIR, f"data/{data_file}.json"), encoding="utf-8", mode='w') as json_data:
            fcntl.flock(json_data, fcntl.LOCK_SH)
            json.dump(payload, json_data)
            fcntl.flock(json_data, fcntl.LOCK_UN)
    except IOError as error:
        raise error


@func_loger
def update_json_file(_file_name: str, *arg):
    """
    Update Json payload
    :param _file_name: File name without the .json
    :param arg: Variables to update
    :return: Returns updated file
    """
    try:
        """load file to modify"""
        payload = load_files(_file_name)
        """update values"""
        payload['value1'] = arg
        payload['value2'] = arg
        payload['value3'] = arg
        """update json file"""
        write_files(payload=payload, data_file=_file_name)
    except Exception as error:
        return error
    return payload
