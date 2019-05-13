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
                    links.append(str(line)[len('b\'href="') +1: str(line).find(">") - 1])
        print(f"liunks: {links}")
        return links

    def get_comments(self, html_file, selector='/html/body/ul/li[{}]/text()[3]'):
        comments = []
        i = 1
        print(i)
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
            # print(link[-10:])
            thumbnails.append(links_template.format(link[-11:]))