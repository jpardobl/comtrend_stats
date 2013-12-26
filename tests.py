from comtrend_stats import read
import logging

logging.basicConfig(level=logging.DEBUG)


def main():
    print(read())


if __name__ == "__main__":
    main()
