'''
Define function 
'''

def decrypt_cypher_text(cypher, key):
    

    new_char = ''
    plain_text = ''
    
    for character in cypher:

        new_char = chr(ord(character)- key)

        plain_text = plain_text + new_char


    return plain_text

print(decrypt_cypher_text('Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu', 3))
    

