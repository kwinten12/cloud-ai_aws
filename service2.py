import boto3
import time

# Create a Transcribe client
transcribe = boto3.client('transcribe', region_name='eu-west-1')
path=input("enter the path to the file (s3://bucket/file): ")

# Use the Transcribe client to transcribe speech from a file
with open('output.mp3', 'rb') as f:
    # Read the file into memory
    mp3_file = f.read()
    
    response = transcribe.start_transcription_job(
        TranscriptionJobName='my_job13',
        LanguageCode='en-US',
        MediaFormat='mp3',
        Media={
            # Pass the file path as a string to the MediaFileUri parameter
            'MediaFileUri': path
        }
    )

# Wait for the transcription job to complete
while True:
    # Get the status of the transcription job
    status = transcribe.get_transcription_job(TranscriptionJobName='my_job13')['TranscriptionJob']['TranscriptionJobStatus']
    
    # If the job is complete, break out of the loop
    if status == 'COMPLETED':
        break
    
    # Sleep for one second before checking the job status again
    time.sleep(1)

# Get the transcribed text from the transcription job
transcribed_text = transcribe.get_transcription_job(TranscriptionJobName='my_job13')['TranscriptionJob']['Transcript']['TranscriptFileUri']

# Print the transcribed text
print(transcribed_text)

# this uri will dowload a json file in wich you can see the text