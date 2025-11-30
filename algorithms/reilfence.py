# algorithms/railfence.py

def RailFenceEncrypt(plaintext, key):
    plaintext = "".join(plaintext.split())
    if key <= 1:
        return plaintext
        
    rail_matrix = [['h' for i in range(len(plaintext))] for j in range(key)]
    direction = False
    row,column = 0
    
    for i in range(len(plaintext)):
        if (row == 0) or (row == key-1):
            direction=not direction 
            
    rail_matrix[row][column]=plaintext[i]
    column+=1
    
    if direction:
        row+=1
    else:
        row-=1
        
cipher_text = []
for k in range(key):
    for p in range(len(plaintext)):
        if rail_matrix[k][p]!='h':
            cipher_text.append(rail_matrix[k][p])
            
return "".join(cipher_text)

def RailFenceDecrypt(ciphertext,key):
    if key <= 1:
        return ciphertext
        
    rail_matrix = [['h' for i in range(len(ciphertext))] for j in range(key)]
    
    direction = False
    row,column = 0
    
    for i in range(len(ciphertext)):
        if (row == 0) or (row == key-1):
            direction=not direction
            
    rail_matrix[row][column]='*'
    column += 1
    if direction:
        row+=1
    else:
        row-=1
        
    index = 0
    for i in range(key):
        for j in range(len(ciphertext)):
            if rail_matrix[i][j] == '*' and index < len(ciphertext):
                rail_matrix[i][j] = ciphertext[index]
                index += 1
                
    plaintext=[]
    direction = False
    row, column =0
    for i in range(len(ciphertext)):
        if (row == 0) or (row == key-1):
            direction=not direction
        plaintext.append(rail_matrix[row][column])
        column+=1
        
        if direction:
            row+=1
        else:
            row-=1
            
    return "".join(plaintext)
