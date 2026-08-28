string1 = input("Enter 1st message: ")
string2 = input("Enter 2nd message: ")
error1 = input("Enter the error position in 1st message (enter -1 if there isn't any): ")
error2 = input("Enter the error position in 2nd message (enter -1 if there isn't any): ")
len1 = len(string1)
len2 = len(string2)
bin_len_1 = ""
bin_len_2 = ""
while len1 > 0:
    if len1 % 2 == 1:
        bin_len_1 = "1" + bin_len_1
    else:
        bin_len_1 = "0" + bin_len_1
    len1 //= 2


while len2 > 0:
    if len2 % 2 == 1:
        bin_len_2 = "1" + bin_len_2
    else:
        bin_len_2 = "0" + bin_len_2
    len2 //= 2

while len(bin_len_1) != 5:
    bin_len_1 = "0" + bin_len_1
while len(bin_len_2) != 5:
    bin_len_2 = "0" + bin_len_2

errors1 = [0, 0, 0, 0, 0]
errors2 = [0, 0, 0, 0, 0]
for i in range(len(string1)):
    if string1[i] == '1':
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

for i in range(len(string2)):
    if string2[i] == '1':
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

string1 = list(string1)
string2 = list(string2)

if int(error1) != -1:
    if string1[int(error1)] == '0':
        string1[int(error1)] = '1'
    else:
        string1[int(error1)] = '0'
if int(error2) != -1:
    if string2[int(error2)] == '0':
        string2[int(error2)] = '1'
    else:
        string2[int(error2)] = '0'

encoded_message = ""
encoded_message += bin_len_1
encoded_message += ''.join(string1)
for i in range(5):
    if errors1[i] == 1:
        encoded_message += "1"
    else:
        encoded_message += "0"
encoded_message += bin_len_2 + ''.join(string2)
for i in range(5):
    if errors2[i] == 1:
        encoded_message += "1"
    else:
        encoded_message += "0"
print("Encoded sequence:", encoded_message)