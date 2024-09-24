import aws_cdk as core
import aws_cdk.assertions as assertions

from 2409_ec2_testing.2409_ec2_testing_stack import 2409Ec2TestingStack

# example tests. To run these tests, uncomment this file along with the example
# resource in 2409_ec2_testing/2409_ec2_testing_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = 2409Ec2TestingStack(app, "2409-ec2-testing")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
