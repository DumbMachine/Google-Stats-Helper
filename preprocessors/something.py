import argparse
import re
import sys
import zipfile as zf
import os


class Takeout:

    def __init__(self, path_takeout=r'C:/Users/ratin/Downloads/', path_extract=None, takeout_names=None, strategy="1"):
        '''
        Initialise the Takeout object.

        @params:
            path_takeout: string
                            Path to folder, where the takeout files have been stored.
            path_extract: string: optional
                            Path to where the extraction should occur.
            takeout_names: list,string: optional
                            If the names of the takeout files are different from the ones given by google.
            strategy: string
                            1: Extract and propcess the data, one-by-one.
                            2: Extract all the files and process data afterwards.
        '''
        self.path_takeout = path_takeout
        self.path_extract = './.data'
        self.zip_files = []
        self.strategy = strategy

    def find_takeout(self):
        '''
        Function to find the takeout files.

        @params:
            None
        '''
        if type(self.path_takeout) == str:
            for _, _, files in os.walk(self.path_takeout):
                for name in files:
                    try:
                        temp_file = re.search(r'\btakeout\b', name).group()
                        if temp_file == 'takeout':
                            self.zip_files.append(name)
                    except:
                        pass
            return self.zip_files
        else:
            raise Exception("Path is not a string.")

    #TODO: Doens't work properly.
    def extractor(self):
        '''
        Function to extract the extractor files.

        @params:
            None
        '''
        self.zip_files = self.zip_files[:1]
        if self.strategy == '1':
            for zip_file in self.zip_files:      
                zip_file = zf.ZipFile(os.path.join(self.path_takeout, zip_file), 'r')
                if not os.path.exists(self.path_extract):
                    os.makedirs(self.path_extract)
                try:
                    zip_file.extractall(self.path_extract)
                except:
                    pass
                zip_file.close()

    def delete(self):
        '''
        Function to delete the extracted files, after use.

        @params:
            None
        '''  
        raise NotImplementedError

    def preprocess(self, path=r'C:\Users\ratin\Downloads\takeout-20190506T143207Z-001\Takeout'):
        '''
        Function to preprocess data, for easier use

        @params:
            None
        ''' 
