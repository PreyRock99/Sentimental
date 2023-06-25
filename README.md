# Sentimental
sentiment analysis using streamlit and huggingface api
# Sentiment-analyser
A sentiment analyser which uses hugging face api to call a sentiment analysis pretrained model and deployed via streamlit for a presentable ui
# Sentiment Analysis using Hugging Face API and Streamlit

This repository contains a sentiment analysis project that utilizes the Hugging Face API for natural language processing and sentiment analysis. The project is deployed using Streamlit, a Python library for creating web applications.

## Overview

Sentiment analysis is the task of determining the sentiment expressed in a given text, whether it is positive, negative, or neutral. In this project, we leverage the power of Hugging Face's pre-trained models to perform sentiment analysis on textual data. The Hugging Face API provides a convenient way to access these models and obtain sentiment predictions.

The project includes a web application built with Streamlit, which allows users to interact with the sentiment analysis model through a user-friendly interface. Users can input text into the application, and the model will predict the sentiment associated with that text.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/sentiment-analysis-huggingface-streamlit.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sentiment-analysis-huggingface-streamlit
   ```

3. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtain an API key from Hugging Face by creating an account on their website (https://huggingface.co).

5. Create a `.env` file in the project root directory and add the following line, replacing `YOUR_API_KEY` with your actual Hugging Face API key:

   ```
   HUGGINGFACE_API_KEY=YOUR_API_KEY
   ```

## Usage

Once you have installed the necessary dependencies and set up your Hugging Face API key, you can run the Streamlit application by executing the following command:

```bash
streamlit run app.py
```

This will start the application, and you should see a URL displayed in the console. Open that URL in your web browser to access the web interface.

In the web interface, you can enter text in the provided input box and click the "Predict" button. The sentiment analysis model will process the input and display the predicted sentiment (positive, negative, or neutral) along with a confidence score.

## Customization

If you want to use a different sentiment analysis model, you can modify the `app.py` file. Look for the section where the Hugging Face API is called to make predictions and replace it with your desired model.

Additionally, you can customize the web interface by modifying the `app.py` file. Streamlit provides a simple and intuitive API for building interactive web applications. You can refer to the Streamlit documentation (https://docs.streamlit.io) for more information on how to customize the application.

## Contributions

Contributions to this project are welcome. If you encounter any issues or have ideas for improvements, feel free to open an issue or submit a pull request on the GitHub repository.



## Disclaimer

Please note that the sentiment analysis predictions provided by this project are based on pre-trained models and may not always be accurate or reflect the true sentiment of the input text. Use the predictions with caution and verify the results before making any critical decisions based on them.

## Acknowledgments

This project is built upon the fantastic work of the Hugging Face team and the Streamlit community. We would like to express our gratitude for their contributions to the field of natural language processing and web application development.
