studentIds = {'knuth': 42.0, 'turing': 56.0, 'nash': 92.0 }
print(studentIds['turing'])

studentIds['nash'] = 'ninety-two'
print(studentIds)

del studentIds['knuth']
print(studentIds)

studentIds['knuth'] = [42.0,'forty-two']
print(studentIds)

print(studentIds.keys() )