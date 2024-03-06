# LangChain Travel Explorer

**LangChain Travel Explorer** is an innovative application designed to help users plan their travels smartly and personalized. Utilizing advanced natural language technologies, such as LangChain and OpenAI, this tool offers travel suggestions based on budget, destination, and interests preferences.

## Project Purpose

This project aims to simplify the travel planning process by integrating artificial intelligence capabilities to provide customized recommendations and travel cost estimates. With **LangChain Travel Explorer**, users can receive detailed suggestions about destinations, activities, and budget planning, all within a user-friendly interface.

## Technologies Used

- LangChain and LangChain OpenAI: For natural language processing and generation.
- Python and libraries like `tavily-python`, `python-dotenv`, among others for backend logic.
- Streamlit: For creating an interactive web interface.
- Tavily: For search and analysis of relevant results.

## Environment Setup

### Prerequisites

- Conda: For virtual environment and dependency management.
- **API Keys**: Valid API keys for OpenAI and Tavily are required for authentication and access to services.

### Obtaining API Keys

Before setting up the environment, you will need to obtain the following API keys:

- **OpenAI API Key**: Register or log in on the [OpenAI website](https://openai.com/api/) to get your API key.
- **Tavily API Key**: Visit the [Tavily portal](https://tavily.com) to request your API key.

Keep these keys safe as they will be needed to set up environment variables.

### Setting Up Environment Variables

After obtaining the API keys, create a `.env` file in the root of your project with the following content, replacing `YOUR_OPENAI_API_KEY` and `YOUR_TAVILY_API_KEY` with the keys you've obtained:

```plaintext
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
TAVILY_API_KEY=YOUR_TAVILY_API_KEY
```

### Configuration Steps

- **Create and Activate the Conda Environment
```plaintext
conda create --name langchain-travel python=3.8
conda activate langchain-travel
```
- **Install Dependencies
```plaintext
pip install -r requirements.txt
```
 

### Running the Project

To run the LangChain Travel Explorer, follow the steps below:

- Navigate to the project directory and run the main script with Streamlit:
```bash
streamlit run main.py
```
- Access the application through the browser at the address indicated by Streamlit (usually http://localhost:8501).
- Enter the details of your trip, including origin, destination, budget, and interests to receive personalized travel suggestions.
