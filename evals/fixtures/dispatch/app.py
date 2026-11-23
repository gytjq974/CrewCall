import argparse

from catalog import SAMPLE_REQUESTS, list_requests, search_requests
from screens import screen_for


HEADING = "접수 현황"


def open_from_list(requests, number):
    for item in list_requests(requests):
        if item.number == number:
            return screen_for(item)
    raise KeyError(number)


def main():
    parser = argparse.ArgumentParser(description="물품 요청 조회")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("list")
    commands.add_parser("search").add_argument("query")
    commands.add_parser("open").add_argument("number")
    args = parser.parse_args()

    if args.command == "open":
        try:
            print(open_from_list(SAMPLE_REQUESTS, args.number))
        except KeyError:
            parser.error("목록에서 요청 번호를 찾을 수 없습니다.")
        return

    if args.command == "search":
        rows = search_requests(SAMPLE_REQUESTS, args.query)
    else:
        rows = list_requests(SAMPLE_REQUESTS)
    print(HEADING)
    for row in rows:
        print(row.number, row.title, row.status, sep=" | ")


if __name__ == "__main__":
    main()
