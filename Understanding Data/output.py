import nbformat

def extract_output(notebook_file):
    with open(notebook_file, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    outputs = []
    for cell in notebook.cells:
        if cell.cell_type == 'code' and 'outputs' in cell:
            outputs.append(cell.outputs)

    return outputs

if __name__ == "__main__":
    notebook_file = "EDA_Venkat Akash Varun Pemmaraju_Understanding Data_.ipynb"  # Replace with your notebook file path
    cell_outputs = extract_output(notebook_file)
    for idx, output in enumerate(cell_outputs, start=1):
        print(f"Output of cell {idx}:")
        for out in output:
            if 'text' in out:
                print(out['text'])
            elif 'data' in out and 'text/plain' in out['data']:
                print(out['data']['text/plain'])
            # Add additional conditions to handle other output formats if needed
        print("="*50)
