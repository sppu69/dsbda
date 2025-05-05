import google.generativeai as genai
import json

# Configure Gemini API
# genai.configure(api_key="AIzaSyD1uTTko4l2i6GEHH-M4vG-9h9b4XGVJyc")

# Create Gemini model
model = genai.GenerativeModel('gemini-2.0-flash')

# Load and number code cells from .ipynb file
def load_numbered_notebook_code(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)

    code_cells = []
    cell_number = 1
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            code = ''.join(cell['source'])
            numbered_code = f"# === Cell {cell_number} ===\n{code}"
            code_cells.append(numbered_code)
            cell_number += 1

    return '\n\n'.join(code_cells)

def chat_about_code(code_content):
    chat = model.start_chat()

    # Send code as initial context
    chat.send_message(f"Here is my Jupyter Notebook code. Each cell is numbered:\n\n{code_content}")

    print("\nChat started! Ask questions about your notebook. Type 'stop' to exit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'stop':
            print("Chat ended.")
            break
        
        response = chat.send_message(user_input)
        print("Gemini:", response.text.strip())

# === MAIN ===
if __name__ == "__main__":
    code_file = "assignment1.ipynb"  # Put your .ipynb file name here
    code_content = load_numbered_notebook_code(code_file)
    chat_about_code(code_content)
