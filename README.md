# Multi_langugae_screeshot_extractor_Model

Multi-Language Screenshot Extractor Model is built using Google Gemini Pro Model, which can be used to solve real-world problems. The Multilanguage extractor can be used to extract information from images, screenshots, invoices, Tax documents images, receipts and so on.
 Streamlit framework is used to create the interactive web application.

 In this project, we can upload images in "jpg", "jpeg", and "png" formats. 

## Gemini Pro: A State-of-the-Art Language Model from Google AI

Key Features:

Multimodal understanding: Processes text, images, audio, and code, unlocking a wide range of capabilities.
Exceptional performance: Achieves state-of-the-art results on various language understanding and generation benchmarks.
Broad capabilities: Generates text, translates languages, writes different creative text formats, and answers your questions in an informative way.
Reasoning and inference: Draws inferences and conclusions, even from incomplete or ambiguous information.
Adaptability: Can be fine-tuned for specific tasks and domains.
Capabilities:

Text generation: Create stories, poems, code, scripts, musical pieces, email, letters, etc.
Question answering: Provide comprehensive and informative answers to open-ended, challenging, or strange questions.
Translation: Translate between different languages with fluency and accuracy.
Summarization: Summarize text documents and generate concise overviews.
Code generation: Write different kinds of creative text formats.
Content creation: Generate different creative text formats, like poems, code, scripts, musical pieces, emails, letters, etc.
Reasoning and inference: Answer your questions in an informative way, even if they are open-ended, challenging, or strange.

### Environment Setup:
1)  create environment:
`conda -p venv python==3.10 -y` (preferably select python version >3.9 as Gemini pro is supported for python >3.9)

2) To activate the environment use:
   `conda activate`
3) Get the GOOGLE_API_KEY from  https://makersuite.google.com/app/apikey

### To Run the app
Prerequisites for running  the application:
- Install the following libraries:

`pip install python-dotenv`

` pip install google-generativeai`

` pip install streamlit`

To run the application: `streamlit run app.py`

#### Final view of the projected hosted on the local host using Streamlit package
![image](https://github.com/sriramkreddy10/Multi_langugae_screeshot_extractor_Model/assets/28749490/8d94fb8e-3c2c-43e8-882b-2dba687c7c00)


#### Example Screenshots:
1) Providing an answer to who sent a smiley emoji in the meeting chat correctly 
![image](https://github.com/sriramkreddy10/Multi_langugae_screeshot_extractor_Model/assets/28749490/f24d9881-ecf7-4e02-93a7-94a258b45a54)


2) Summarize the text present in the slide of the screenshot

![image](https://github.com/sriramkreddy10/Multi_langugae_screeshot_extractor_Model/assets/28749490/3221f2d3-3dee-489b-8e5b-a8b5e0916bf6)



