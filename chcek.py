with open('results.txt','r') as log:
        f=log.read() 
        #testCASE
        word1='The.result.*testcase (.*) is.+.FAILED'
        word2='The.result.*testcase (.*) is.+.ERRORED'
        word3='Testcase.result.for(.*) is.+.PASSED'
        word4='The.result.*testcase (.*) is.+.ABORTED'
print(word3)