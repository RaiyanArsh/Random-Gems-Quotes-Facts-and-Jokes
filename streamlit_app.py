import streamlit as st
import requests
import random
import string
import clipboard

# Create a sidebar with options
option = st.sidebar.radio("Select an Option", ["Quote Generator","Dad Jokes", "Facts"])
api_key = 'CByiyC/dvwHHxZO0YhBxQA==zBktfyMh9t1adxJm'  # Replace with your actual API key

# Function to fetch a random quote
def fetch_random_quote(category):
     # Default category for quotes
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    headers = {'X-Api-Key': api_key}
    response = requests.get(api_url, headers=headers)
    if response.status_code == requests.codes.ok:
        data = response.json()  
        try :
            quote = data[0]["quote"]
            author = data[0]["author"]
            st.write(quote)
            st.write(f'Author : {author}')
        except : 
            st.write('Servers are busy come back later')
    else:
        return "Error fetching quote", ""

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def jokes():

    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/dadjokes?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if(st.button('Generate')):
        if response.status_code == requests.codes.ok:
            data = response.json()
            st.write(data[0]["joke"])
        else:
            st.write("Error:", response.status_code, response.text)

def facts() :
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if(st.button("Generate")):
        if response.status_code == requests.codes.ok:
            data = response.json()
            st.write(data[0]["fact"])
        else:
            st.write("Error:", response.status_code, response.text)

def riddles():
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok:
        # print(response.text)
        data = response.json()
        return data
        st.write(data)
        ques = data[0]['question']
        st.write(ques)
        ans = data[0]['answer']
        if(st.button('Reveal Answer')):
            st.write(ans)
    else:
        st.write("Error:", response.status_code, response.text)


# Main app logic based on user's choice
if option == "Quote Generator":
    st.title("Quote Generator")
    category = st.selectbox("Select a Category", ["happiness","family","failure","experience", "friendship","knowledge","Leadership","men","movies","success", "love", "life"]) 
    if(st.button('Generate Random Quote')) :
        fetch_random_quote(category)
        # st.write(f'"{quote}" - {author}')4

elif option == "Password Generator":
    st.title("Password Generator")
    password_length = st.slider("Select Password Length", 4, 32, 12)
    generated_password = generate_random_password(password_length)
    st.write(f'Generated Password: {generated_password}')
    if st.button("Copy Password"):
        clipboard.copy(generated_password)  # Copy the password to the clipboard
        st.success("Password Copied to Clipboard")

elif option == "Dad Jokes" :
    st.title("Dad Jokes")
    jokes()


elif option == "Riddles" :
    if st.button('Generate'):
        riddle_data = riddles()
        if riddle_data is not None:
            ques = riddle_data[0]['question']
            question_container = st.empty()
            question_container.write(ques)
        
        if st.button('Reveal Answer'):
            ans = riddle_data[0]['answer']
            question_container.empty()  # Clear the question
            st.write(f"Answer: {ans}")
elif option == "Facts" :
    st.title("Random Facts")
    facts()
