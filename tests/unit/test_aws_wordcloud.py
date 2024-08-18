"""
Unit tests to verify the functionality of the aws-wordcloud service.
"""

import os
import sys

import aws_cdk as core
import aws_cdk.assertions as assertions
import pytest

from aws_wordcloud.aws_wordcloud_stack import AWSWordCloudStack

# Adds tests/unit/packages to the system path.
# This must be done before importing any modules from the packages directory.
sys.path.append(os.path.join(os.path.dirname(__file__), "packages"))

# Adds lambda/create to the system path.
# This must be done before importing any modules from the packages directory.
project_root_dir = os.path.join(os.path.dirname(__file__), "..", "..")
sys.path.append(os.path.abspath(os.path.join(project_root_dir, "lambda", "create")))

from wordcloud_handler import WordCloudHandler


# example tests. To run these tests, uncomment this file along with the example
# resource in aws_wordcloud/aws_wordcloud_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AWSWordCloudStack(app, "aws-wordcloud")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })


def test_wordcloud_generation():
    """
    Tests whether the generation of a word cloud returns a valid HTTP status
    code.
    """

    print("Testing word cloud generation")
    handler = WordCloudHandler()
    event = ' { "text": "This is a word cloud test" } '
    context = ""
    handler_result = handler(event, context)
    assert handler_result.get("statusCode") == 200  # HTTP OK


if __name__ == "__main__":
    pytest.main()
