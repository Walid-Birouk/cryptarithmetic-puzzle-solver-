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
st.title('Cryptarithmetic Puzzle Solver')

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
    
    st.write(solution)