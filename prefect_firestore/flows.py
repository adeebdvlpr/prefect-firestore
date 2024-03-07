"""This is an example flows module"""
from prefect import flow

from prefect_firestore.blocks import FirestoreBlock
from prefect_firestore.tasks import (
    goodbye_prefect_firestore,
    hello_prefect_firestore,
)


@flow
def hello_and_goodbye():
    """
    Sample flow that says hello and goodbye!
    """
    FirestoreBlock.seed_value_for_example()
    block = FirestoreBlock.load("sample-block")

    print(hello_prefect_firestore())
    print(f"The block's value: {block.value}")
    print(goodbye_prefect_firestore())
    return "Done"


if __name__ == "__main__":
    hello_and_goodbye()
