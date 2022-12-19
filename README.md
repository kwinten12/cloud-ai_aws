# cloud-ai_aws (r0855665, Kwinten Van Houtven)

## service1.py
This file uses the polly service to transform a text to speech.
The code is build so that you only have to run the code and specify via the console what text you want to transform.
Next the program will generate a file 'output.mp3' in the folder where the code was ran.

## service2.py
In this program we used the aws transcribe service to transform a spoken text to a string.
To use this program u need to run the code and specify the path to a public s3 bucket contain the (public) mp3 file you want to transform.
Once you ran this code a link will apear in the console, you can then click this link to download a json file containing the transformed text.
Be sure that you use the public uri in the shape of s3://bucket/file as path. 
