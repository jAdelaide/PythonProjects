                    # Need file 'unicorns.txt'
file = open("unicorns.txt", "rt")
data = file.read()
words = data.split()

print "The word count in the file 'unicorns.txt' is:", len(words)

#############################################################################
                    # As a Lambda function:
#import boto3
#
#def lambda_handler(event, context):
#    s3 = boto3.client('s3')
#    data = s3.get_object(Bucket='748unicorns', Key='unicorns.txt')
#    contents = data['Body'].read()
#    words = contents.split()
#    return "The word count in the file 'unicorns.txt' is " + str(len(words))

