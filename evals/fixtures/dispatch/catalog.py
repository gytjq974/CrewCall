from dataclasses import dataclass


@dataclass(frozen=True)
class Request:
    number: str
    title: str
    status: str
    urgent: bool = False


SAMPLE_REQUESTS = (
    Request("R-101", "작업 장갑", "접수"),
    Request("R-102", "안전모", "보류", urgent=True),
    Request("R-103", "절연 장갑", "완료"),
)


def list_requests(requests):
    return list(requests)


def search_requests(requests, query):
    return [item for item in requests if query.casefold() in item.title.casefold()]
