'''
Define function decrypt_cypher_text.
Function will pass a cypher text of string data type and key value of integer data type.
The function will decrypt cypher text using key and return plain text
of string data type.
'''

def decrypt_cypher_text(cypher, key):
    

    new_char = ''
    plain_text = ''
    
    for character in cypher:

        new_char = chr(ord(character)- key)

        plain_text = plain_text + new_char


    return plain_text
# Test string Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu
# Expected output: Each error you make in programming is an opportunity to become a better developer
print(decrypt_cypher_text('Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu', 3))

    

