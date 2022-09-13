import requests


class DirectMailClient:

    def __init__(self, token: str) -> object:
        self._token = token
        self._headers = {
            "Accept": "application/json",
            "Authorization": f"Basic {token}"
        }

    def get(self, url: str) -> object:
        return requests.get(url, headers=self._headers).json()

    def get_projects(self) -> dict:
        res = dict()
        projects = self.get("https://secure.directmailmac.com/api/v2/projects")
        for project in projects:
            res[project['document_identifier']] = project['name']
        return res

    def get_reports(self, project: str) -> dict:
        res = dict()
        reports = self.get(f"https://secure.directmailmac.com/api/v2/projects/{project}/reports")
        for report in reports:
            res[report['uuid']] = report['title']
        return res

    def who_viewed(self, project: str, report: str) -> list:
        recipients = self.get(f"https://secure.directmailmac.com/api/v2/projects/{project}/reports/{report}/recipients")
        return [recipient['email'] for recipient in recipients]

    def who_clicked(self, project):
        # TODO
        return
