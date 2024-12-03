# Madlibs Generator 🖋️

This is a fun **Madlibs Generator** project that allows users to fill in placeholders in a story template to create their own unique and hilarious story! 🚀

## 📋 Overview

The program reads a story template from a text file, identifies placeholders enclosed in `<` and `>`, and prompts the user to replace them with words of their choice. Once all placeholders are replaced, the completed story is displayed.

## 🛠 Features

- **Dynamic Placeholder Detection**: Automatically detects all placeholders in the story template.
- **Interactive Input**: Prompts the user to provide words for each placeholder.
- **Customized Story**: Generates a unique story based on user inputs.
- **Duplicate-Free Placeholders**: Ensures each unique placeholder is asked only once.

## 🚀 How It Works

1. **Prepare a Story Template**:
   - Write a story in `story.txt` with placeholders enclosed in `<` and `>` (e.g., `<noun>`, `<verb>`).
2. **Run the Script**:
   - The program will prompt you to provide replacements for the placeholders.
3. **Enjoy the Story**:
   - The program replaces the placeholders with your inputs and prints the customized story.

## 📦 Example

### Input Template (`story.txt`):

```plaintext
Once upon a time, there was a <adjective> <noun> who loved to <verb> in the <place>.
```
