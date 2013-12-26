import requests
import os, sys
import logging
from BeautifulSoup import BeautifulSoup
import simplejson


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


def read(router_ip, router_user, router_pass):
    url = os.path.join("http://%s" % router_ip, "statswan.cmd")
    logging.debug("Connecting to %s" % url)
    response = requests.get(url, auth=(router_user, router_pass, ))
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
    if len(sys.argv) != 4:
        logging.error("Not enough arguments, need: router_ip, router_user, router_password")
        exit(1)
    ret = read(sys.argv[1], sys.argv[2], sys.argv[3])
    if ret is None:
        exit(1)
    print ret
    exit(0)
