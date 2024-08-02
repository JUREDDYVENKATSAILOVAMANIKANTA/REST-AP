#!/usr/bin/env python
# coding: utf-8

# In[2]:


def process_request(request):
    # Initialize the response dictionary with the static values
    response = {
        "is_success": True,
        "user_id": "Manikanta.Jureddy",
        "email": "jj3741@srmist.edu.in",
        "roll_number": "RA2111003010837"
    }
    
    # Extract the data from the request
    data = request.get("data", [])
    
    # Separate numbers and alphabets from the data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Determine the highest alphabet
    highest_alphabet = max(alphabets) if alphabets else None
    
    # Update the response dictionary with the processed values
    response["numbers"] = numbers
    response["alphabets"] = alphabets
    response["highest_alphabet"] = [highest_alphabet] if highest_alphabet else []
    
    return response

# Example request
request = {
    "data": ["A", "C", "z"]
}

# Process the request
response = process_request(request)
print(response)


# In[3]:


def process_request(request):
    # Initialize the response dictionary with the static values
    response = {
        "is_success": True,
        "user_id": "Manikanta.Jureddy",
        "email": "jj3741@srmist.edu.in",
        "roll_number": "RA2111003010837"
    }
    
    # Extract the data from the request
    data = request.get("data", [])
    
    # Separate numbers and alphabets from the data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Determine the highest alphabet
    highest_alphabet = max(alphabets) if alphabets else None
    
    # Update the response dictionary with the processed values
    response["numbers"] = numbers
    response["alphabets"] = alphabets
    response["highest_alphabet"] = [highest_alphabet] if highest_alphabet else []
    
    return response

# Example request
request = {
    "data": ["2", "4", "5", "92"]
}

# Process the request
response = process_request(request)
print(response)


# In[5]:


def process_request(request):
    # Initialize the response dictionary with the static values
    response = {
        "is_success": True,
        "user_id": "Manikanta.Jureddy",
        "email": "jj3741@srmist.edu.in",
        "roll_number": "RA2111003010837"
    }
    
    # Extract the data from the request
    data = request.get("data", [])
    
    # Separate numbers and alphabets from the data
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    
    # Determine the highest alphabet
    highest_alphabet = max(alphabets) if alphabets else None
    
    # Update the response dictionary with the processed values
    response["numbers"] = numbers
    response["alphabets"] = alphabets
    response["highest_alphabet"] = [highest_alphabet] if highest_alphabet else []
    
    return response

# Example request
request = {
    "data": ["M", "1", "334", "4", "B"]
}

# Process the request
response = process_request(request)
print(response)


# In[ ]:




