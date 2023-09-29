import streamlit as st
from simpleai.search import CspProblem, backtrack

# Define the constraints
def constraint_unique(variables, values):
    # All values must be unique
    return len(values) == len(set(values))

def constraint_problem(variables, values):
    # The problem constraint 
    sum1 = sum([values[variables.index(letter)] * 10**(len(word1) - i - 1) for i, letter in enumerate(word1)])
    sum2 = sum([values[variables.index(letter)] * 10**(len(word2) - i - 1) for i, letter in enumerate(word2)])
    sum3 = sum([values[variables.index(letter)] * 10**(len(word3) - i - 1) for i, letter in enumerate(word3)])
    # Ensure that the first letter of each word does not map to zero
    if values[variables.index(word1[0])] == 0 or values[variables.index(word2[0])] == 0 or values[variables.index(word3[0])] == 0:
        return False
    return sum1 + sum2 == sum3

# Streamlit code
st.set_page_config(page_title='Cryptarithmetic Puzzle Solver', page_icon="🧩", layout='wide', initial_sidebar_state='auto')


st.title('Cryptarithmetic Puzzle Solver 🧩')

# Create columns for input and output
input_col, output_col = st.columns(2)

with input_col:
    st.markdown("""
    Enter each word in the puzzle. Each letter represents a unique digit. 
    The goal is to find a substitution of digits into letters that makes the equation true.
    """)

    # Get user input
    word1 = st.text_input("Enter the first word: ").upper()
    word2 = st.text_input("Enter the second word: ").upper()
    word3 = st.text_input("Enter the third word: ").upper()

if st.button('Solve'):
    # Define the variables
    letters = list(set(word1 + word2 + word3))
    
    # Define the domains
    domains = {letter: list(range(10)) for letter in letters}
    
    # Define the problem
    constraints = [
        (letters, constraint_unique),
        (letters, constraint_problem),
    ]
    
    problem = CspProblem(letters, domains, constraints)
    
    # Solve the problem
    solution = backtrack(problem)
    
    with output_col:
        if solution is not None:
            # Format and print the solution
            word1_solution = ''.join(str(solution[letter]) for letter in word1)
            word2_solution = ''.join(str(solution[letter]) for letter in word2)
            word3_solution = ''.join(str(solution[letter]) for letter in word3)
            
            st.markdown(f"## Solution 💡")
            st.markdown(f"**{word1}** becomes **{word1_solution}**")
            st.markdown(f"**{word2}** becomes **{word2_solution}**")
            st.markdown(f"**{word3}** becomes **{word3_solution}**")
            
            st.markdown(f"**{word1}**` `+` `**{word2}**` `=` `**{word3}**")
            st.markdown(f"**{word1_solution}**` `+` `**{word2_solution}**` `=` `**{word3_solution}**")

            
        else:
            st.markdown("## No Solution 💔")
