def is_palindrome(s):
    rev = ''.join(reversed(s))
    if s == rev:
        return True
if __name__ == "__main__":
  pass  
s = "potop"
ans = is_palindrome(s)

if (ans):
    print("Yes")
else:
    print("No")