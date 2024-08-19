# String 변수에 Hello World 문자열 저장
mystring = "Hello World"
# 문자열 출력
print (mystring)
# Indexing & Slicing
print (mystring[0]) # H
print (mystring[-1]) # d

# Slicing
mystring_new = "abcdefghijk"
# 문자열 출력
print (mystring_new)
# Slicing
print (mystring_new[2:]) # cdefghijk
print (mystring_new[2:5]) # cde (자기 자신을 제외한 거기 때문에 f X)

# Step 추가한 Slicing
print (mystring_new[::2]) # a c e g i k
print (mystring_new[::-1]) # 역순으로 출력
# Slicing을 통해 반복문을 간결하게 나타낼 수 있다.