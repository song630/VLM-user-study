import os, sys
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm
import json
import random


main_dir = f'/Users/song630/intern/VLM-user-study/sampled/pose_large_sdxl_225'
json_file = f'{main_dir}/selected_text_prompt_200.json'


def read_json():
    with open(json_file) as f:
        data = json.load(f)
    print(f'Loaded {len(data)} prompts from {json_file}.')
    return data  # format: {filename: prompt, filename: prompt, ...}


def sample_user_study_data():
    json_data = read_json()
    filenames = list(json_data.keys())
    # save filenames and prompts to a txt:
    with open(f'{main_dir}/sample_prompts.txt', 'w') as f:
        for filename in filenames:
            prompt = json_data[filename]
            f.write(f'{filename}: {json_data[filename]}\n')
    # save categories to a txt:
    with open(f'{main_dir}/sample_categories.txt', 'w') as f:
        for filename in filenames:
            prompt = json_data[filename]
            # every prompt has a substring of 'view of killer whale 35mm photograph';
            # get the category name between 'view of' and '35mm photograph':
            category = prompt.split('view of ')[1].split(' 35mm photograph')[0]
            f.write(f'{filename}: {category}\n')


if __name__ == '__main__':
    sample_user_study_data()
    print('Done.')
