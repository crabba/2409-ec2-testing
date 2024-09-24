import aws_cdk as core
import aws_cdk.assertions as assertions

from ec2_testing_2409.ec2_testing_2409_stack import Ec2Testing2409Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in ec2_testing_2409/ec2_testing_2409_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Ec2Testing2409Stack(app, "ec2-testing-2409")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
