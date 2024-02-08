import os
import typer
import openai
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

openai.api_key = "API KEY"
# print("API KEY: ",os.getenv("OPENAI_KEY"))
app = typer.Typer()

@app.command()
def interactive_chat(
    text: Optional[str] = typer.Option(None, "--text", "-t", help="Start with text"),
    temperature: float = typer.Option(0.7, help="Control Randomness. Defaults to 0.7"),
    max_tokens: int = typer.Option(
        150, help="Control length of response. Defaults to 150"
    ),
    model: str = typer.Option(
        "gpt-3.5-turbo-0125", help="Control the model to use. Defaults to gpt-3.5-turbo-0125"
    ),
):
    """Interactive CLI tool to chat with ChatGPT."""
    typer.echo(
        "Starting interactive chat with ChatGPT. Type 'EOF' on a new line to submit your input, type 'exit' to end the session."
    )

    messages = []

    while True:
        if text:
            prompt = text
            text = None
        else:
            prompt_lines = []
            typer.echo("You: (Type your message. Type 'EOF' on a new line when done)")
            while True:
                line = input()
                if line == "EOF":
                    break
                prompt_lines.append(line)
            prompt = "\n".join(prompt_lines)

        messages.append({"role": "user", "content": prompt})
        if prompt.lower() == "exit":
            typer.echo("ChatGPT: Goodbye!")
            break

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        typer.echo(f'ChatGPT: {response["choices"][0]["message"]["content"]}')
        messages.append(response["choices"][0]["message"])

if __name__ == "__main__":
    app()