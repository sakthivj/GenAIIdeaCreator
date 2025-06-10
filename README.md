# GenAI Product Ideator

## Overview
The GenAI Product Ideator is a web application designed to help users generate innovative product ideas using Generative AI. By leveraging OpenAI's API, the application provides detailed product concepts based on user-defined topics or domains. The application is built using Streamlit, making it easy to deploy and use in a web browser.

## Features
- User-friendly interface for inputting topics or domains.
- Generates comprehensive product ideas including:
  - Overview of the concept
  - Innovative angles and differentiation
  - Suggested features tailored to real-time customer needs
  - Recommended technology stack
  - Target users and their benefits
  - Potential business impact
  - Challenges and considerations for implementation
  - Future enhancements or iterations
  - Market trends alignment

## Installation Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GenAI-IdeaDesribe.git
   ```
2. Navigate to the project directory:
   ```
   cd GenAI-IdeaDesribe
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
   Ensure you have Streamlit and OpenAI's Python client library installed.

4. Set up your OpenAI API key:
   - Create a `.streamlit/secrets.toml` file in the project directory and add your API key:
     ```
     [OPENAI_API_KEY]
     key = "your_openai_api_key"
     ```

## Usage Guidelines
1. Run the application:
   ```
   streamlit run Main.py
   ```
2. Open your web browser and navigate to `http://localhost:8501` to access the application.
3. Enter a topic or domain in the input field and click the "Generate Idea" button to receive a detailed product concept.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.