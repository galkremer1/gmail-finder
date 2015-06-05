__author__ = 'galkremer'
import os
import argparse
import sys
import getopt
import oauth2client

from datetime import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import client
from oauth2client import tools

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail Name Finder'

def get_credentials():
    """
    Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print 'Storing credentials to ' + credential_path
    return credentials

def print_usage():
    print 'Usage: find_name.py --text <text>'

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"ht:",["help", "text="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(2)

    query = ''
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif opt in ("-t", "--text"):
            query = arg

    credentials = get_credentials()
    service = build('gmail', 'v1', http=credentials.authorize(Http()))

    if not query:
        query=raw_input("Please enter the text to search for: ")

    print "Searching for: {}".format(query)

    response = service.users().messages().list(userId='me', q=query).execute()
    times = response['resultSizeEstimate']
    if times==0:
        print "The query you searched for is not found in your gmail inbox."
    elif times==1:
        print "The query you searched for was mentioned in 1 email in your gmail inbox."
    else:
        print "Your query was mentioned in %d emails in your gmail inbox." %times

if __name__ == '__main__':
    main(sys.argv[1:])
