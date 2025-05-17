import glob
import gzip
import json
import math
import yaml
import os
import os.path as osp
import pickle
import random
import string
import threading
from collections import defaultdict
from itertools import groupby
from typing import Any, Dict, Literal, Optional, Union

import tqdm
from PIL import Image


def load_json(path):
    file = open(path, "r")
    return json.loads(file.read())


def load_gzip(path):
    file = gzip.open(path, "r")
    return json.loads(file.read())


def load_image(file_name):
    return Image.open(file_name).convert("RGB")


def load_pickle(path):
    file = open(path, "rb")
    data = pickle.load(file)
    return data


def write_gzip(data, output_path):
    with gzip.open(output_path, "wt") as f:
        json.dump(data, f)

def write_json(data, output_path):
    file = open(output_path, "w")
    file.write(json.dumps(data))


def load_gz_dataset(path, dataset_size):
    file = gzip.open(path, "r")
    print(type(file))
    for l in file:
        print(type(l), "first element")
        break
    data = [line for line in tqdm(file, total=dataset_size)]
    return data


def save_pickle(data, output_path):
    file = open(output_path, "wb")
    pickle.dump(data, file)


def load_yaml(path):
    return yaml.safe_load(open(path))


def save_image(image, path):
    img = Image.fromarray(image)
    img.save(path)
