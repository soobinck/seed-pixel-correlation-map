import os


def mask_filtered_files(root_dir):
    mask = None
    filtered = []
    for root, dirs, files in os.walk(root_dir, topdown=False):
        for file in files:
            if file.endswith('raw') or file.endswith('tif'):
                if 'Mask' in file:
                    mask = os.path.join(root, file)
                else:
                    filtered.append({'root': root, 'file': file})

    return mask, filtered
