import json  
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
  
# Function to detect language using Azure AI with JSON input  
def language_detection_example(client, input_json):  
    try:  
        # Parsing the JSON input to extract the text documents  
        input_documents = json.loads(input_json)["documents"]  
        # Detecting the language of the input text  
        response = client.detect_language(documents=input_documents, country_hint='us')  
          
        # Preparing the JSON output  
        output = {"results": []}  
        for doc in response:  
            output["results"].append({  
                "id": doc.id,  
                "language": doc.primary_language.name,
                "confidenceScore": doc.primary_language.confidence_score 
            })  
        return json.dumps(output, indent=4)  
    except Exception as err:  
        # Handling any exceptions (errors) that occur  
        print("Encountered exception. {}".format(err))  
        return json.dumps({"error": str(err)})  
  
# Authenticate the client  
client = authenticate_client()  
  
# JSON input with an array of text documents  
input_json = '''  
{  
    "documents": [  
        {"id": "1", "text": "Buenos días a todos"},  
        {"id": "2", "text": "Bonjour à tous"},  
        {"id": "3", "text": "Guten Morgen an alle"},  
        {"id": "4", "text": "Buongiorno a tutti"},  
        {"id": "5", "text": "Bom dia a todos"},  
        {"id": "6", "text": "Доброе утро всем"},  
        {"id": "7", "text": "大家早上好"},  
        {"id": "8", "text": "皆さん、おはようございます"},  
        {"id": "9", "text": "सभी को सुप्रभात"},  
        {"id": "10", "text": "صباح الخير للجميع"}  
    ]  
}  
'''  
  
# Calling the function with the client and JSON input  
output_json = language_detection_example(client, input_json)  
  
# Outputting the JSON result  
print(output_json)  