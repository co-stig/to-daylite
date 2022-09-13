import requests


class DayliteClient:

    def __init__(self, token: str) -> object:
        self._token = token
        self._headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self._token}"
        }

    def get(self, url: str) -> object:
        return requests.get(url, headers=self._headers).json()

    def post(self, url: str, payload: object) -> object:
        return requests.post(url, headers=self._headers, json=payload).json()

    def get_contacts(self) -> dict:
        mapping = dict()
        all_contacts = self.get("https://api.marketcircle.net/v1/contacts")
        for contact in all_contacts:
            url = contact['self']
            details = self.get(f"https://api.marketcircle.net{url}")
            for email in details.get('emails', list()):
                address = email['address']
                if address not in mapping:
                    mapping[address] = list()
                mapping[address].append(url)
        return mapping

    def create_or_update_group(self, group_name: str, contacts: list, owner_user_id="1000") -> None:
        print(f"Will create group '{group_name}' with users {contacts}, owned by {owner_user_id}")
        owner_url = f"/v1/users/{owner_user_id}"
        self.post("https://api.marketcircle.net/v1/groups", payload={
            "name": group_name,
            "owner": owner_url,
            "creator": owner_url,
            "contacts": [{"contact": contact} for contact in contacts]
        })
