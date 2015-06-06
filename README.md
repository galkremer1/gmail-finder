# gmail-finder
> Search your Google Inbox for messages containing a string

## Overview

This project uses google gmail API in order to search for a string in the user Gmail's inbox.
You will either enter a string through cli arguments or be prompted one.

This program will then tell you how many messages (if any) contain your given string.

## Installation

```sh
# Clone this repository
$ git clone https://github.com/galkremer1/gmail-finder.git

# Install python sdk
$ pip install --upgrade google-api-python-client
```

You will need to enable the [Gmail API](https://developers.google.com/gmail/api/quickstart/python#step_1_enable_the_api_name)

Follow the provided steps as described and make sure to include the client_secret.json in the same folder.

## Code Example
```sh
$ python find_name.py
# You will be prompted for a query string

$ python find_name.py --text string
# Search you inbox for a string
```

## API Reference

[Google's Gmail API](https://developers.google.com/gmail/api/quickstart/python).

## License

MIT License
