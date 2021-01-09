from pathlib import Path


class CreateBatch:
    def __init__(self, datatype):
        self.datatype = datatype

        self.create_batch_file()

    def create_batch_file(self):
        my_bat = open(Path.cwd()/self.datatype/"read_pkl.bat", "w+")
        pkl_reader_path = Path(Path.cwd())/'open_pkl.py'
        my_bat.write(f'@python {str(pkl_reader_path)} %*\n@pause')
        my_bat.close()
