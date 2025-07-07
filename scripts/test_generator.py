import subprocess
import os

def run_ollama(code_path, yaml_path, output_path):
    # Read code and YAML instruction
    with open(code_path, 'r') as code_file, open(yaml_path, 'r') as yaml_file:
        code = code_file.read()
        prompt = yaml_file.read()

    # Combine both into one prompt
    full_prompt = f"{prompt}\n\n---\n\n{code}"

    print("🔄 Sending prompt to Ollama...")

    # Run Ollama and pass the prompt via stdin
    result = subprocess.run(
        ["ollama", "run", "codellama"],
        input=full_prompt.encode('utf-8'),
        capture_output=True,
        check=True  # raises error if execution fails
    )

    # Decode the response
    output = result.stdout.decode('utf-8')

    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the result
    with open(output_path, "w", encoding='utf-8') as out_file:
        out_file.write(output)

    print(f"✅ Test generated and saved to {output_path}")


# Paths relative to script location
run_ollama("../input/input.cpp", "../prompts/generate_tests.yaml", "../tests/test_main.cpp")

