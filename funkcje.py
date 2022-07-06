def is_palindrome(s):
    rev = ''.join(reversed(s))
    return s == s[::-1]


if __name__ == "__main__":
  s = "potop"
  ans = is_palindrome(s)

  if ans:
    print("Yes")
  else:
    print("No")
  pass

