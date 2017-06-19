lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [c1 + c2 +p1 + p2 for c1 in digits for c2 in digits for p1 in lowercase for p2 in lowercase]
