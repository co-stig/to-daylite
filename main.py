import configparser
from daylite import DayliteClient
from direct_mail import DirectMailClient

DAYLITE_TOKEN = ""
DIRECT_MAIL_AUTH = ""


def initialize():
    global DAYLITE_TOKEN
    global DIRECT_MAIL_AUTH
    config = configparser.ConfigParser()
    config.read('settings.ini')
    settings = config['Settings']
    DAYLITE_TOKEN = settings['DaylightToken']
    DIRECT_MAIL_AUTH = settings['DirectMailToken']


def filter_contacts_by_mail(contacts, emails):
    res = list()
    for email in emails:
        for url in contacts.get(email, list()):
            res.append(url)
    return res


if __name__ == '__main__':
    initialize()
    daylite_client = DayliteClient(DAYLITE_TOKEN)
    direct_mail_client = DirectMailClient(DIRECT_MAIL_AUTH)
    contacts = daylite_client.get_contacts()
    projects = direct_mail_client.get_projects()
    for project_id in projects:
        reports = direct_mail_client.get_reports(project_id)
        for report_id in reports:
            viewers = filter_contacts_by_mail(contacts, direct_mail_client.who_viewed(project_id, report_id))
            daylite_client.create_or_update_group(reports[report_id] + ": Viewed", viewers)
