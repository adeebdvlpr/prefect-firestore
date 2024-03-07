from prefect import flow

from prefect_firestore.tasks import (
    goodbye_prefect_firestore,
    hello_prefect_firestore,
)


def test_hello_prefect_firestore():
    @flow
    def test_flow():
        return hello_prefect_firestore()

    result = test_flow()
    assert result == "Hello, prefect-firestore!"


def goodbye_hello_prefect_firestore():
    @flow
    def test_flow():
        return goodbye_prefect_firestore()

    result = test_flow()
    assert result == "Goodbye, prefect-firestore!"
