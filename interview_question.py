data ="""1. Muhammad Ali | muhammad_ali@gmail.com
3. Muthu  | muthu123@hotmail.com
2. Tan Ah Hock | ah_hock666@gmail.com
4. Peter Garden | peter.g@outlook.com
5. Paul Steve | paul.steve92@gmail.com
6. Mary Ho | marry_ho99@gmail.com
7. Jane Tan | jane.tan123@gmail.com
"""

expected_outcome = [
    {
        'name': 'Muhammad Ali', 
        'email': 'muhammad_ali@gmail.com'
    }, 
    {'name': 'Muthu', 'email': 'muthu123@hotmail.com'}, 
    {'name': 'Tan Ah Hock', 'email': 'ah_hock666@gmail.com'}, 
    {'name': 'Peter Garden', 'email': 'peter.g@outlook.com'}, 
    {'name': 'Paul Steve', 'email': 'paul.steve92@gmail.com'}, 
    {'name': 'Mary Ho', 'email': 'marry_ho99@gmail.com'}, 
    {'name': 'Jane Tan', 'email': 'jane.tan123@gmail.com'}, 
    {'name': '', 'email': ''}
    ]
