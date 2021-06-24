import os
import time
import requests 
import pandas as pd


def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


if __name__ == '__main__':
    df = pd.read_json("data/feeds.json.gz")
    dst_folderpath = "data/gtfs_transitland"

    t0 = time.time()
    for idx, row in df.iterrows():
        if row['url'] is not None:
            dst_filepath = os.path.join(
                dst_folderpath,
                f"{idx}.zip")
            if not os.path.exists(dst_filepath):
                try:
                    download_url(row['url'], dst_filepath)
                    duration = time.time() - t0
                    print(f"{idx}, {duration:.2f}: {row['url']}")
                except Exception as e:
                    print(f"{idx}, {type(e)}, {e}")
