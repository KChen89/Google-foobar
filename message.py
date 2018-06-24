import base64
MESSAGE='''EEIeEA0EBhsWSUtfTUIJFQYJEUlHRUoGAQsPDQQJHgBKRVRHRA0WGg4AAAAKQE9IQgsNAwIXGhRE SF9OTAwDBhwCBwEHAg5CQUVJBgAADAsdAAAAABNESF9OTBADCQEECA0BSUdFShcPBQEBER1MRVdF SRQCDgBJR0VKAwEIREhfTkwSBAtPQB4='''
KEY='kemengchen'
result=list()
for i,c in enumerate(base64.b64decode(MESSAGE)):
	result.append(chr(ord(c)^ord(KEY[i%len(KEY)])))
print ''.join(result)