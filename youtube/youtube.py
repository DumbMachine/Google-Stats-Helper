import json
import os
from lxml import html


class Youtube:

    def __init__(self):

        self.path = '../.data/takeout-20190506T143207Z-001/Takeout/YouTube/'    # Static for now.
        self.comments_path = os.path.join(self.path, 'my-comments/my-comments.html')

    def get_links(self):
        links = []
        with open(self.comments_path, 'rb') as file:
            # print(len(file.read().splitlines()))
            for line in file.read().splitlines()[0].split():
                if 'href' in str(line):
                    links.append(str(line)[len('b\'href="') + 1: str(line).find(">") - 1])
        print(f"liunks: {links}")
        return links

    def get_comments(self, html_file, selector='/html/body/ul/li[{}]/text()[3]'):
        comments = []
        i = 1
        with open(html_file, 'rb') as file:
            hmm_file = html.parse(file)
            # something = hmm_file.xpath(selector.format(i))[0]
            # print(something)

            while(True):
                try:
                    comments.append(hmm_file.xpath(selector.format(i))[0])
                    i += 1
                    print(something)
                except:
                    return comments
        return comments

    def get_thumbnail(self):
        thumbnails = []
        links_template = "https://img.youtube.com/vi/{}/0.jpg"
        links = self.get_links()
        for link in links:
            thumbnails.append(links_template.format(link[-11:]))
        return thumbnails

    def get_youtube_history(self):
        '''
        Function to preprocess youtube history data

        @params:
            None

        @returns:
            .json
            with all the required info for the futher things
        '''
        something = {'one': []}
        with open(os.path.join(self.path, 'history/search-history.html'), 'rb') as file:
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
        with open('./something/youtube.json', 'w') as outfile:
            json.dump(something, outfile)

    def youtube_subscriptions(self):
        subscriptions = {'data': []}
        with open(r'C:\Users\ratin\Desktop\Google-Stats-Helper\.data\takeout-20190506T143207Z-001\Takeout\YouTube\subscriptions\subscriptions.json', encoding="utf8") as something:
            big_json = json.load(something)
            for smal__json in big_json:
                print(smal__json['snippet']['description'])
                subscriptions['data'].append({
                    'channel': smal__json['snippet']['title'],
                    'desc': smal__json['snippet']['description'],
                    'thumbnails': smal__json['snippet']['thumbnails']['high']['url'],
                    'total_vids': smal__json['contentDetails']['totalItemCount'],

                })

        with open('./subs.json', 'w') as outfile:
            json.dump(subscriptions, outfile)