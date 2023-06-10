import os
import shutil
import json

GRF_FILE = "sals_canalboats_ex.grf"
PATH_DEF_FILE = "path_def.json"

THIS_DIR = os.path.dirname(__file__)

def install():
    if not os.path.exists(os.path.join(THIS_DIR, GRF_FILE)):
        return
    else:
        # check path_def.json
        if not os.path.exists(os.path.join(THIS_DIR, PATH_DEF_FILE)):
            return
        with open(os.path.join(THIS_DIR, PATH_DEF_FILE), "r") as charstream:
            _path_def = json.load(charstream)
        install_prefix = _path_def["install_prefix"]
        install_prefix = os.path.normpath(os.path.expanduser(install_prefix))

        src_file = os.path.join(THIS_DIR, GRF_FILE)
        dst_file = os.path.join(install_prefix, GRF_FILE)
        os.makedirs(os.path.dirname(dst_file), exist_ok=True)
        shutil.copy(src_file, dst_file)

if __name__ == "__main__":
    install()
