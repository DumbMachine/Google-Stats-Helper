import json
import argparse
import re
import sys
import zipfile as zf
import os
# from bs4 import BeautifulSoup
from lxml import html


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

        self._xpath_search_gap_title = '/html/body/div/div[{}]/div/div[2]'
        self._xpath_search_gap_product = '/html/body/div/div[{}]/div/div[4]'
        # self._xpath_search_gap = None
        # self._xpath_search_gap = None
        # self._xpath_search_gap = None
        # self._xpath_search_gap = None

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
        raise NotImplementedError

    def search_history(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Google Apps\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/apps.json', 'w') as outfile:
            json.dump(something, outfile)

    def search_gmail(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Gmail\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/gmail.json', 'w') as outfile:
            json.dump(something, outfile)

    def search_developer(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Developers\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/Developers.json', 'w') as outfile:
            json.dump(something, outfile)

    def search_books(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Books\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/Books.json', 'w') as outfile:
            json.dump(something, outfile)

    def play_games(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Google Play Games\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/games.json', 'w') as outfile:
            json.dump(something, outfile)

    def play_video_search(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Video Search\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/video.json', 'w') as outfile:
            json.dump(something, outfile)

    def shopping(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Shopping\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/shopping.json', 'w') as outfile:
            json.dump(something, outfile)

    def news(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\News\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')[12:]
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'news': str(html_file.xpath('/html/body/div/div[1]/div/div[1]/p')[0].text_content().encode('ascii', 'ignore')),
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/news.json', 'w') as outfile:
            json.dump(something, outfile)

    def cs(self):
        '''
        Function to preprocess history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        # SEARHC in GOOGLE APPS:
        something = {'one': []}
        with open(os.path.join(self.path_extract, r'Takeout\My Activity\Google Analytics\My Activity.html'), 'rb') as file:
            html_file = html.parse(file)
            i = 0
            while i < 100:
                try:
                    for content, content1 in zip(html_file.xpath(self._xpath_search_gap_title.format(i)), html_file.xpath(self._xpath_search_gap_product.format(i))):
                        title = content.text_content().encode('ascii', 'ignore')
                        hmm = content1.text_content().encode('ascii', 'ignore')
                        print(f"Title: {title}")
                        print(f"{hmm}")
                        something["one"].append({
                            'Search': str(title),
                            'App': str(hmm),
                        })
                    i += 1
                except:
                    break
        with open('./something/cs.json', 'w') as outfile:
            json.dump(something, outfile)