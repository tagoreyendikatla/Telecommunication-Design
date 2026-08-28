code = input("Enter the encoded sequence: ")
len1 = 0
for i in range(5):
    len1 = len1*2 + int(code[i])
obs_message1 = ""
for i in range(5, 5 + len1):
    obs_message1 += code[i]
obs_parity1 = [0, 0, 0, 0, 0]
for i in range(5 + len1, 10 + len1):
    obs_parity1[i - 5 - len1] = int(code[i])
len2 = 0
for i in range(10 + len1, 15 + len1):
    len2 = len2*2 + int(code[i])
obs_message2 = ""
for i in range(15 + len1, 15 + len1 + len2):
    obs_message2 += code[i]
obs_parity2 = [0, 0, 0, 0, 0]
for i in range(15 + len1 + len2, 20 + len1 + len2):
    obs_parity2[i - 15 - len1 - len2] = int(code[i])

errors1 = [0, 0, 0, 0, 0]
errors2 = [0, 0, 0, 0, 0]
for i in range(len(obs_message1)):
    if obs_message1[i] == '1':
        a = ""
        j = i + 1
        while j > 0:
            if j % 2 == 1:
                a = "1" + a
            else :
                a = "0" + a
            j //= 2
        while len(a) != 5:
            a = "0" + a
        for j in range(5):
            if a[j] == '1':
                errors1[j] += 1
for i in range(5):
    if errors1[i] % 2 == 0:
        errors1[i] = 0
    else:
        errors1[i] = 1

for i in range(len(obs_message2)):
    if obs_message2[i] == '1':
        a = ""
        j = i + 1
        while j > 0:
            if j % 2 == 1:
                a = "1" + a
            else :
                a = "0" + a
            j //= 2
        while len(a) != 5:
            a = "0" + a
        for j in range(5):
            if a[j] == '1':
                errors2[j] += 1
for i in range(5):
    if errors2[i] % 2 == 0:
        errors2[i] = 0
    else:
        errors2[i] = 1
        
diff1 = [0, 0, 0, 0, 0]
diff2 = [0, 0, 0, 0, 0]
for i in range(5):
    if errors1[i] != obs_parity1[i]:
        diff1[i] = 1
for i in range(5):
    if errors2[i] != obs_parity2[i]:
        diff2[i] = 1

error_bit1 = 0
error_bit2 = 0
for i in range(5):
    error_bit1 = error_bit1*2 + diff1[i]
    error_bit2 = error_bit2*2 + diff2[i]

error_bit1 -= 1
error_bit2 -= 1

print("Observed message-1:", obs_message1)
print("Observed message-2:", obs_message2)

actual_message1 = ""
actual_message2 = ""

if error_bit1 == -1:
    actual_message1 = obs_message1
else:
    temp1 = list(obs_message1)
    temp1[error_bit1] = str(1 - int(temp1[error_bit1]))
    actual_message1 = ''.join(temp1)

print("Actual message-1:", actual_message1)

if error_bit2 == -1:
    actual_message2 = obs_message2
else:
    temp2 = list(obs_message2)
    temp2[error_bit2] = str(1 - int(temp2[error_bit2]))
    actual_message2 = ''.join(temp2)

print("Actual message-2:", actual_message2)