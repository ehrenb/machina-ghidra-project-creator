import base64
import glob
import json
from pprint import pformat
from pathlib import Path
import shutil

from machina.core.ghidra_worker import GhidraWorker

class GhidraProjectCreator(GhidraWorker):
    types = [
        'elf',
        'pe'
    ]
    next_queues = []

    def __init__(self, *args, **kwargs):
        super(GhidraProjectCreator, self).__init__(*args, **kwargs)
        self.logger.debug(pformat(self.config))

    def callback(self, data, properties):

        data = json.loads(data)

        # resolve path
        target = self.get_binary_path(data['ts'], data['hashes']['md5'])
        self.logger.info(f"resolved path: {target}")

        self.analyze_headless(
            str(Path(target).parent),
            f'proj-{data["hashes"]["md5"]}-{self.cls_name}',
            import_files=[target]
        )