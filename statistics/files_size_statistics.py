import base64
import json
import os
import subprocess

import pandas as pd

from statistics.constants.constants import CSV_FILE_PATH


class ProcessData:

    def generate_files_data(self, path):
        os.chmod('./utils/scripts/list_directory_info.sh', 0o777)
        subprocess.call(['./utils/scripts/list_directory_info.sh', path])
        df = pd.read_csv(CSV_FILE_PATH, sep='\t', header=None)
        df.columns = ['size', 'name']
        return df

    def get_average(self, path):
        df = self.generate_files_data(path)
        size = df['size'].mean()
        result = json.dumps(['averageSize', {'mean': size}])
        print("response="+result)
        return result

    def get_biggest(self, path):
        df = self.generate_files_data(path)
        name = df._get_value(df['size'].idxmax(), 'name')
        size = df['size'].max()
        result = json.dumps(['biggestFile', {'name': name, 'size': size}])
        print("response=" + result)
        return result

    def get_smallest(self, path):
        df = self.generate_files_data(path)
        name = df._get_value(df['size'].idxmin(), 'name')
        size = df['size'].min()
        result = json.dumps(['smallestFile', {'name': name, 'size': size}])
        print("response=" + result)
        return result

    def get_histogram(self, path):
        df = self.generate_files_data(path)
        result = df['size'].hist()
        return result

    def get_histogramBase64(self, path):
        df = self.generate_files_data(path)
        ax = self.get_histogram(path)
        fig = ax.get_figure()
        fig.savefig('cache/hist.png', format='png')
        with open('cache/hist.png', 'rb') as img_file:
            b64_string = base64.b64encode(img_file.read())
        print(b64_string)
        result = json.dumps(['histogram', {'pngBase64': str(b64_string)}])
        return result
