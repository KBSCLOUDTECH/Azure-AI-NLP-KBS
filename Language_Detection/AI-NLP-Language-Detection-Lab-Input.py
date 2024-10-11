from azure.ai.textanalytics import TextAnalyticsClient  
from azure.core.credentials import AzureKeyCredential  

  
  
language_key = "067be37a98ed4a6a88991c2d7aabb876"  
language_endpoint = "https://ai-3003-kbs-la.cognitiveservices.azure.com/"   
  
# Function to authenticate the Azure Text Analytics client  
def authenticate_client():  
    ta_credential = AzureKeyCredential(language_key)  
    text_analytics_client = TextAnalyticsClient(  
            endpoint=language_endpoint,  
            credential=ta_credential)  
    return text_analytics_client  
  
# Function to detect language using Azure AI with user input  
def language_detection_example(client, input_text):  
    try:  
        # The user's input text is passed as a document to the Azure service  
        documents = [input_text]  
        # Detecting the language of the input text  
        response = client.detect_language(documents=documents, country_hint='us')[0]  
        # Printing the name of the detected language  
        print("Language: ", response.primary_language.name)  
    except Exception as err:  
        # Handling any exceptions (errors) that occur  
        print("Encountered exception. {}".format(err))  
  
# Authenticate the client  
client = authenticate_client()  
  
# Loop to prompt the user to enter text multiple times  
while True:  
    # Prompt the user to enter text for language detection  
    input_text = input("Enter the text you'd like to analyze: ")  
      
    # Calling the function with the client and user input  
    language_detection_example(client, input_text)  
      
    # Ask if the user wants to analyze another piece of text  
    repeat = input("Do you want to analyze another text? (yes/no): ")  
    if repeat.lower() != 'yes':  
        break  
