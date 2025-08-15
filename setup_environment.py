import os
import sys

def main():
    # Print current Python environment details
    print(f"Python version: {sys.version}")
    print(f"Python path: {sys.executable}")
    
    # Check if baml-py is installed
    try:
        import baml_py
        print(f"baml-py version: {baml_py.__version__}")
    except ImportError:
        print("baml-py is not installed in the current environment.")
        
    # Check if OpenAI API key is set
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    if openai_api_key:
        print("OPENAI_API_KEY is set")
    else:
        print("OPENAI_API_KEY is not set - this will be needed to run the ExtractResume function")

if __name__ == "__main__":
    main()
