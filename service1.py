import boto3

# Create a new Amazon Polly client
polly = boto3.client(service_name='polly', region_name='eu-west-1')

# Specify the text to synthesize

text = str(input('what text do you want to format to an mp3: '))

# Call the synthesize_speech method to create an audio file
response = polly.synthesize_speech(
    Text=text,
    OutputFormat='mp3',
    VoiceId='Joanna'
)

# Save the audio file
with open('output.mp3', 'wb') as file:
    file.write(response['AudioStream'].read())

