from urllib.parse import urlparse, parse_qs
import json


def parse_signed_attempt_from_url(url):

    urlObject = urlparse(url)
    signedAttempt = parse_qs(urlObject.query)['signedAttempt']

    return json.loads(signedAttempt[0])


