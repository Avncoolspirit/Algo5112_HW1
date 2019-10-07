

def respacing_rec(s,wordlist):
	print s, len(s)
	for i in range(0,len(s)+1):
		print s[0:i]
		if s[0:i] in wordlist:
			if i == len(s):
				print "True string" ,s[0:i]
				return True
			print s[0:i],s[i:len(s)]
			if respacing_rec(s[i:len(s)],wordlist):
				return True
		
	return False



def respacing (s, wordlist):
	sentence = []
	test =''
	for char in s:
		test+=char
		if test in wordlist:
			sentence.append(test)
			test=''
	if "".join(sentence) != s:
		return ""
	return "" if "".join(sentence) != s else  " ".join(sentence)

test_result = respacing_rec('glenndialtruckglennglen' ,['menu', 'turbo', 'york', 'cork', 'glen', 'haven', 'glenn', 'warm', 'dial', 'truck'])

print test_result
# with open("respace_tests.txt", 'r') as testfile:
#     L = testfile.readlines()
#     num_tests_run = 0
#     success=0
#     for l in L:
#         values = l.strip().split(";")
#         testname = values[0]
#         wordlist = values[1]
#         string = values[2]
#         expected_respace = values[3]
#         wordlist = wordlist.split(",")
#         testcase = (testname, wordlist, string, expected_respace)
#         test_result = respacing_rec(proudsellsailsellproud ,['suse', 'isle', 'sell', 'wars', 'proud', 'flood', 'sail', 'mar', 'depot', 'pda'])
#         if test_result==expected_respace:
#             success+=1
#             print "success",num_tests_run,success, expected_respace, test_result
#         else:
#             print test_result, string, wordlist,expected_respace
#         num_tests_run += 1
