from langchain.text_splitter import CharacterTextSplitter
from typing import List
from io import StringIO
import csv

class CSVTextSplitter(CharacterTextSplitter):
    def __init__(self, csv_separator=",", **kwargs):
        super().__init__(**kwargs)
        self.csv_separator = csv_separator

    def split_text(self, text: str) -> List[str]:
        reader = csv.reader(StringIO(text), delimiter=self.csv_separator)
        titles = next(reader)
        contents = list(reader)
        docs = []
        for row in contents:
            new_entries = []
            for i, entry in enumerate(row):
                new_entries.append(titles[i] + "：" + entry)
            docs.append("，".join(new_entries))
        return docs
