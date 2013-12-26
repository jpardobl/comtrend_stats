from comtrend_stats import read
import logging

logging.basicConfig(level=logging.DEBUG)

ROUTER_IP = "192.168.1.1"
ROUTER_USER = "1234"
ROUTER_PASSWORD = "password"


def main():
    print(read(ROUTER_IP, ROUTER_USER, ROUTER_PASSWORD))


if __name__ == "__main__":
    main()
