def fetch_request(send, number):
    try:
        return send("GET", f"/requests/{number}")
    except TimeoutError:
        return send("GET", f"/requests/{number}")


def submit_request(send, payload):
    # 서버가 응답 전에 접수를 끝냈을 수 있다. 재전송하면 접수가 중복된다.
    return send("POST", "/requests", payload)
