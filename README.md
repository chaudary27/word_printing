# Word Printing - FRIEND ASCII Art Generator

## Overview

This interactive Python program (`file.py`) prints any word made up of the letters **F, R, I, E, N, D** in a fun ASCII art style. Each letter is displayed as a 5x5 grid of asterisks, side by side, creating a visual representation of your word!

---

## How It Works

1. **Run the program**: The script will prompt you to enter a word using only the letters F, R, I, E, N, D (uppercase).
2. **Type your word**: For example, try `FRIEND`, `FIRE`, or `END`.
3. **See the magic!**: The program prints your word in ASCII art.
4. **Exit anytime**: Type `exit` to end the session.

---

## Example Output

Input:
```
FRIEND
```
Output:
```
*****  *****  *****  *****  *   *  ***** 
*      *   *    *    *      **  *  *   *
*****  *****    *    *****  * * *  *   *
*      *   *    *    *      *  **  *   *
*      *   *  *****  *****  *   *  *****
```

Visual Example:

```
*****   *****   *****   *****   *   *   *****
*       *   *     *     *       **  *   *   *
*****   *****     *     *****   * * *   *   *
*       *   *     *     *       *  **   *   *
*       *   *   *****   *****   *   *   *****
```

---

## Usage Instructions

1. Make sure you have Python installed.
2. Open a terminal in the `word_printing` directory.
3. Run:
   ```
   python file.py
   ```
4. Enter words using only the letters F, R, I, E, N, D (uppercase).
5. Type `exit` to quit.

---

## Features

- Only accepts uppercase letters from the word **FRIEND**.
- Prints a friendly error message for invalid input.
- ASCII art is generated in real-time for each valid word.
- Keeps running until you type `exit`.

---

## Example Session

```
Enter words with letters F, R, I, E, N, D or Type exit to end: FIND
*****  *****  *****  *****
*      *   *    *    *   *
*****  *****    *    *   *
*      *   *    *    *   *
*      *   *  *****  *****

Enter words with letters F, R, I, E, N, D or Type exit to end: END
*****  *****  *****
*      *      *   *
*****  *****  *   *
*      *      *   *
*      *****  *****

Enter words with letters F, R, I, E, N, D or Type exit to end: exit
Thankyou for Playing
```

---

## Notes

- Only uppercase letters are accepted.
- Any other input will show an error message.

---

## Author

Made with ❤️ for learning and fun!