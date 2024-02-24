## Cryptarithmetic Puzzle Solver Streamlit App

A Streamlit application designed to solve cryptarithmetic puzzles. Cryptarithmetic puzzles are a type of mathematical game where the digits are replaced by letters. Each letter represents a unique digit, and the goal is to find the digit each letter represents such that the given equation holds true.

## <span>Ⅰ.</span> Application Overview

The Cryptarithmetic Puzzle Solver app provides an interactive platform where users can input a cryptarithmetic puzzle and receive a solution. The application uses the `simpleai` library's constraint satisfaction problem (CSP) solver to find a valid solution for the input puzzle.

### Key Features

- **User Input for Puzzle Words**: Users can enter three words representing the cryptarithmetic puzzle. The app is designed to solve puzzles in the format of "WORD1 + WORD2 = WORD3".
- **Constraint Satisfaction Problem Solving**: The app employs the CSP solving technique to find a solution that satisfies all constraints, including unique digit representation and correct arithmetic calculation.

- **Solution Display**: If a solution exists, the app displays the original words with letters replaced by the corresponding digits, demonstrating the valid arithmetic operation.

## <span>Ⅱ.</span> How It Works

1. **Defining Constraints**: Two primary constraints are defined:

   - `constraint_unique`: Ensures all letters represent unique digits.
   - `constraint_problem`: Validates the arithmetic equation by converting letters to digits and checking if the sum is correct, including the condition that the first letter of any word cannot represent zero.

2. **Streamlit Interface**:
   - **Page Configuration**: Set with a puzzle-themed title and icon.
   - **User Input**: Users input the three words of the puzzle in designated text fields.
   - **Solution Process**: Upon clicking the 'Solve' button, the app processes the input, applies CSP with backtracking to find a solution, and displays the outcome in the output column.

## <span>Ⅲ.</span> Implementation Details

- The `simpleai.search.CspProblem` and `backtrack` function are used to define and solve the puzzle.
- The puzzle words are processed to identify unique letters, which serve as variables in the CSP.
- Domains for each variable are digits from 0 to 9, with constraints applied to ensure a valid and unique solution.
- The solution, if found, is displayed by mapping each letter to its corresponding digit, showing both the original and solved equations.

## <span>Ⅳ.</span> Solution Display

- **Successful Solution**: The app shows the original words with their corresponding numeric values, illustrating how the puzzle's equation holds true with the found digit substitutions.
- **No Solution**: In cases where no solution exists given the constraints, the app informs the user that no solution can be found.

## <span>Ⅴ.</span> Conclusion

The Cryptarithmetic Puzzle Solver Streamlit app is an engaging tool that combines the fun of puzzle-solving with the power of programming and artificial intelligence. By leveraging CSP and backtracking algorithms, it offers an automated solution to what is traditionally a manually intensive puzzle type. This app demonstrates the practical application of AI techniques in recreational mathematics and provides a user-friendly interface for puzzle enthusiasts to test and solve cryptarithmetic challenges.
