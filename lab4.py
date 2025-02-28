str = input("Enter the string: ")
vowels = "aeiouAEIOU"
count = 0
for char in str:
 if char in vowels:
 count += 1
print("The numbers of vowels in the string is : ",count)


str = input("Enter the str to convert: ")
lowercase_result = ""
for char in str:
 if 'A' <= char <= 'Z':
 lowercase_result += chr(ord(char)+32)
 else:
 lowercase_result += char
print("lowercase string: ",lowercase_result)

str1 = input("Enter the first string :")
str2 = input("Enter the second string: ")
found = False
for i in range(len(str1)-len(str2)+1):
 if str[i:i+len(str2)] ==str2:
 found = True
 break
if found:
 print(str2,"is present in",str1)
else:
 print("Not present")

string =input("Enter the string: ")
removestring =input("Enter the char to remove: ")
final = string.replace(removestring, "")
print(final)
