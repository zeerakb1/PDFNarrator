import argparse
import PyPDF2
from gtts import gTTS


def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


def text_to_speech(text, output_file):
    tts = gTTS(text)
    tts.save(output_file)


def main(pdf_file, output_file):
    text = extract_text_from_pdf(pdf_file)
    text_to_speech(text, output_file)
    print(f"Audio file saved as {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to Audio")
    parser.add_argument("pdf_path", help="Path to the PDF file")
    parser.add_argument("audio_name", help="Name of the output audio file")

    args = parser.parse_args()

    main(args.pdf_path, args.audio_name)