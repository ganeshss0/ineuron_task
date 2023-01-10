import re
import os
import sys
from collections import OrderedDict

try:
    import PyPDF2 as pdf
    import docx2txt as d2t
    import striprtf.striprtf as rtf
    import numpy as np
    import pandas as pd
except:
    raise ModuleNotFoundError("Required modules 'PyPDF2', 'docx2txt', 'striprtf', 'pandas', type `pip install PyPDF2 docx2txt striprtf pandas`")
    
class data_extraction:

    '''This class extract links, email from pdf, docx, rtf files'''
    

    def __init__(self, folder_dest: str) -> None:
        if os.path.isdir(folder_dest):
            self.folder = os.path.abspath(folder_dest)
            self.Links = []
            self.pattern()
        else:
            raise FileNotFoundError(f'{folder_dest} path does not exists.')


    def pattern(self, pats: dict = {}, *args) -> None:

        '''Takes a dictonary of like {'name' : 'regular expression'} to find that regular expression in all files.'''

        self.patterns = OrderedDict(
            github = re.compile(r'(?:https:\/\/)?[w\.]*(?:github.com/)[\S]+'),
            linkedin = re.compile(r'(?:https:\/\/)?[w\.]*(?:linkedin.com/)[\S]+'),
            kaggle = re.compile(r'(?:https:\/\/)?[w\.]*(?:kaggle.com/)[\S]+'),
            email = re.compile(r'[\S]+@[\S]+\.[\S]+'))

        for pat in pats:
            self.patterns[pat] = re.compile(re.escape(pats[pat]))

        self.columns = ['fileName'] + list(self.patterns.keys())

        
    def extract_links(self) -> object:

        '''Return instance after extracting all the links from all files.'''

        for root, dirs, files in os.walk(self.folder):
            for file in files:
                path = os.path.join(root, file)
                if file.endswith('.pdf'):
                    text = self.pdf_to_text(path)
                elif file.endswith('.docx'):
                    text = self.docx_to_text(path)
                elif file.endswith('.rtf'):
                    text = self.rtf_to_text(path)
                else:
                    continue
                links = self.text_to_links(text, file)
                self.links_to_array(links)

        self.Links = self.Links.T
        return self


    def pdf_to_text(self, path: str, *args) -> str:

        '''Return a string after converting all the data inside a pdf file to string.'''

        file = pdf.PdfReader(path)
        length = len(file.pages)
        text = ''
        for i in range(length):
            text += file.pages[i].extract_text()
        return text
        

    def docx_to_text(self, path: str, *args) -> str:

        '''Return a string after converting all the data inside a docx file to string.'''

        return d2t.process(path)


    def rtf_to_text(self, path: str, *args) -> str:

        '''Return a string after converting all the data inside a rtf file to string.'''

        with open(path) as file:
            text = rtf.rtf_to_text(file.read())
        return text


    def text_to_links(self, text: str, fileName: str, *args) -> list:

        '''Return a list after extracting all links from a string.'''

        links = []
        self.__Max = 1
        for pattern in self.patterns:
            if (n:= re.findall(self.patterns[pattern], text)):
                LINK = list(set(n))
                if (l:= len(LINK)) > self.__Max:
                    self.__Max = l

                links.append(LINK)
            else:
                links.append([None])
        
        return [[fileName] * self.__Max] + links


    def links_to_array(self, data: list) -> None:

        '''Convert all data in numpy array after making all the columns of equal lenght.'''

        try:
            self.__Max
        except:
            self.__Max = len(data[0])
        
        for i in range(len(data)):
            if (n := len(data[i])) < self.__Max:
                data[i].extend([None] * (self.__Max - n))

        if len(self.Links) > 0:
            self.Links = np.concatenate((self.Links, data), axis = 1)
        else:
            self.Links.extend(data)


    def to_DataFrame(self) -> pd.DataFrame:

        '''Return a pandas Dataframe from the extracted links.'''

        if self.Links == []:
            self.extract_links()
        
        return pd.DataFrame(self.Links, columns = self.columns)
