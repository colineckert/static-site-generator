import os
import shutil

def copy_static_files():
    if os.path.exists('public'):
        shutil.rmtree('public')
    os.mkdir('public')
    copy_contents('static', 'public')


def copy_contents(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        print(f'Copying {src_path} to {dest_path}')

        if os.path.isdir(src_path):
            copy_contents(src_path, dest_path)
        else:
            shutil.copy(src_path, dest_path)
            print(f'Copied {src_path} to {dest_path}')
