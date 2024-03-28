from typing import NamedTuple, Optional

import requests


class CuboxResponse(NamedTuple):
    message: str
    code: int


class Cubox:
    def __init__(self, api_link, show_message=False):
        self.api_link = api_link
        self.show_message = show_message

    def save_link(self, url: str, title: str, description: Optional[str] = "", tags=None,
                  folder: Optional[str] = "") -> CuboxResponse:
        if tags is None:
            tags = []
        payload = {
            "type": "url",
            "content": url,
            "title": title,
            "description": description,
            "tags": tags,
            "folder": folder
        }
        response = requests.post(self.api_link, json=payload)
        data = response.json()
        if self.show_message:
            print(f'code={data["code"]}, message={data["message"]}')
        return CuboxResponse(data["message"], data["code"])

    def save_memo(self, content: str, title: Optional[str] = "", description: Optional[str] = "",
                  tags=None, folder: Optional[str] = "") -> CuboxResponse:
        if tags is None:
            tags = []
        payload = {
            "type": "memo",
            "content": content,
            "title": title,
            "description": description,
            "tags": tags,
            "folder": folder
        }
        response = requests.post(self.api_link, json=payload)
        data = response.json()
        if self.show_message:
            print(f'code={data["code"]}, message={data["message"]}')
        return CuboxResponse(data["message"], data["code"])


if __name__ == '__main__':
    cubox = Cubox("https://cubox.pro/c/api/save/a3npONzvgwE")

    cubox.save_link("https://www.google.com", "Google", "Search Engine", ["search", "engine"], "add link test")

    cubox.save_memo("This is a memo", "Memo", "This is a memo", ["memo"], "add memo test")
