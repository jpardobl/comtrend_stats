import requests
import os
import logging
from BeautifulSoup import BeautifulSoup
import simplejson


ROUTER_IP = "192.168.1.1"
ROUTER_USER = "1234"
ROUTER_PASSWORD = "password"

POSITIONS = {
    "ETH0.3_B_RCVD": 16,
    "ETH0.3_P_RCVD": 17,
    "ETH0.3_ERROR_RCVD": 18,
    "ETH0.3_DROPS_RCVD": 19,
    "ETH0.3_B_TRANS": 20,
    "ETH0.3_P_TRANS": 21,
    "ETH0.3_ERROR_TRANS": 22,
    "ETH0.3_DROPS_TRANS": 23,

    "ETH0.2_B_RCVD": 26,
    "ETH0.2_P_RCVD": 27,
    "ETH0.2_ERROR_RCVD": 28,
    "ETH0.2_DROPS_RCVD": 29,
    "ETH0.2_B_TRANS": 30,
    "ETH0.2_P_TRANS": 31,
    "ETH0.2_ERROR_TRANS": 32,
    "ETH0.2_DROPS_TRANS": 33,

    "ETH0.6_B_RCVD": 36,
    "ETH0.6_P_RCVD": 37,
    "ETH0.6_ERROR_RCVD": 38,
    "ETH0.6_DROPS_RCVD": 39,
    "ETH0.6_B_TRANS": 40,
    "ETH0.6_P_TRANS": 41,
    "ETH0.6_ERROR_TRANS": 42,
    "ETH0.6_DROPS_TRANS": 43,


}


def read():
    url = os.path.join("http://%s" % ROUTER_IP, "statswan.cmd")
    logging.debug("Connecting to %s" % url)
    response = requests.get(url, auth=(ROUTER_USER, ROUTER_PASSWORD, ))
    if response.status_code != 200:
        logging.error("Cannot retrieve data, status_code: %d; response: \n%s" %
            (response.status_code, response.text))
        return None
    soup = BeautifulSoup(response.text)
    logging.debug("Router Response:\n%s\n" % soup)
    tds = soup.findAll("td")
    logging.debug("retrieved tds (length:%d): %s" % (len(tds), tds))

    ret = {}
    for k, v in POSITIONS.items():
        logging.debug("Collecting k: %s , val: %d" % (k, v))
        ret[k] = int(tds[POSITIONS[k]].contents[0])

    return simplejson.dumps(ret)


if __name__ == "__main__":
    ret = read()
    if ret is None:
        exit(1)
    print ret
    exit(0)
