from typing import Union
from typing import Dict
from typing import Any

import logging
import boto3
from botocore.exceptions import ClientError

OPTIONAL_DICT = Union[None, Dict[str, Any]]
AWS_QUEUE = Dict[str, str]


logger = logging.getLogger(__name__)
sqs = boto3.resource("sqs")


def create_queue(
    name: str,
    tags: OPTIONAL_DICT = {},
    attributes: OPTIONAL_DICT = {},
) -> AWS_QUEUE:
    """
    Creates a SQS queue.

    Args:
        name (str): name of the SQS queue to create
        attributes (dict): maximum message size or whether it is a FIFO

    Returns:
        A Queue object that contains metadata about the queue and that can
        be used to peform queue operations like sending and receiving
        messages.
    """
    try:
        queue = sqs.create_queue(
            QueueName=name,
            Attributes=attributes,
            tags=tags,
        )
        logger.info(f"Created queue '{name}' with URL='{queue.url}'")
    except ClientError as error:
        logger.exception(f"Couldn't create queue named '{name}'")
        raise error
    else:
        return queue
