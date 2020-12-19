from collections import defaultdict
words = []
tags = []
tagsCount = defaultdict(lambda: int(0))
wordCount = defaultdict(lambda: int(0))
wordsTagsCount = defaultdict(lambda: int(0))
bigramCount = defaultdict(lambda: int(0))
_3Count = defaultdict(lambda: int(0))
_4Count = defaultdict(lambda: int(0))
_5Count = defaultdict(lambda: int(0))
def clearsent(sent, flag):
	pre = len(sent)
	sent = sent.replace("।", " ")
	sent = sent.replace("  ", " ")
	sent = sent.replace(" _", "_")
	while(pre != len(sent)):
	    pre = len(sent)
	    sent = sent.replace("  ", " ")
	ll = []
	tag = []
	for i in sent.split():
	    wordsTagsCount[i] += 1
	    temp = i.split("_")
	    ll.append(temp[0])
	    if flag:
	        wordCount[temp[0]] += 1
	    if "_".join(temp[1:]) != "":
	        tag.append("_".join(temp[1:]))
	        if flag:
	            tagsCount["_".join(temp[1:])] +=1
	if flag:
	    words.extend(ll)
	    tags.extend(tag)
	return(ll)
def bigrams(sent,flag):
    ll = clearsent(sent, flag)
    bgms = []
    for j in range(0, len(ll)):
        if (j + 1 < len(ll)):
            bgms.append(ll[j] + " "+ ll[j+1])
            if flag:
                bigramCount[ll[j] + " "+ ll[j+1]] +=1
    return(bgms)

def trigrams(sent,flag):
    ll = clearsent(sent, 0)
    bgms = []
    for j in range(0, len(ll)):
        if (j + 2 < len(ll)):
            bgms.append(ll[j] + " "+ ll[j+1] + " "+ ll[j+2])
            if flag:
                _3Count[ll[j] + " "+ ll[j+1] + " "+ ll[j+2]] += 1
    return(bgms)



def _4grams(sent,flag):
    ll = clearsent(sent, 0)
    bgms = []
    for j in range(0, len(ll)):
        if (j + 3 < len(ll)):
            
            bgms.append(ll[j] + " "+ ll[j+1] +" "+ ll[j+2] + " "+ ll[j+3])
            if flag:
                _4Count[ll[j] + " "+ ll[j+1] +" "+ ll[j+2] + " "+ ll[j+3]] +=1
    return(bgms)

def _5grams(sent,flag):
    ll = clearsent(sent, 0)
    bgms = []
    for j in range(0, len(ll)):
        if (j + 4 < len(ll)):
            bgms.append(ll[j] + " "+ ll[j+1] +" "+ ll[j+2] + " "+ ll[j+3]  +  " "+ ll[j+4])
            if flag:
                _5Count[ll[j] + " "+ ll[j+1] +" "+ ll[j+2] + " "+ ll[j+3]  +  " "+ ll[j+4]] += 1
    return(bgms)

    return(bgms)
def ttp():
	fttp = open("TTP.txt", "w",encoding="utf8")
	for i in tagsCount.keys():
	    for j in tagsCount.keys():
	        if (i):
	            cji = 0
	            for k in range(1, len(tags)):
	                if(tags[k] == i and tags[k-1] == j):###p(ti|ti-1) = p(i|j)
	                    cji += 1
	            fttp.write("{} {} {}\n".format(i,j,str(cji/tagsCount[j])))
	fttp.close()
def wep():
	fwep = open("WEP.txt", "w",encoding="utf8")
	for i in wordsTagsCount.keys():
	    temp = i.split("_")
	    tag = "_".join(temp[1:])
	    if tag != "":
	        fwep.write("{} {} {}\n".format(temp[0],tag,str(wordsTagsCount[i]/tagsCount[tag])))
	    else:
	    	fwep.write("{} {} {}\n".format(temp[0],tag,str(wordsTagsCount[i]/tagsCount[prev])))
	    prev = tag
	fwep.close()
def prplex(ll,ngramCount):
    perplexity = 1
    count = 0
    prob= defaultdict(lambda: int(0))
    for i in ngramCount.keys():
        temp= i.split()
        prob[i] = ngramCount[i] /(wordCount[temp[-1]])
    for i in ll:
        try:
            perplexity *= pow(prob[i], (-1/len(prob.keys())))
        except:
            count+=1
            
    return(perplexity )
def perplex():
	fwr = open('Perplexity.txt', "w", encoding="utf8")
	sent = "<s> जब_PR मेरे_PR पास_N_NST एक_QT पैसा_N_NN नहीं_RP </s>"
	fwr.write(sent+"\n")
	ll = bigrams(sent, 0)
	fwr.write("Bigram perplexity  = " + str(prplex(ll,bigramCount)))
	fwr.write("\n")
	ll = trigrams(sent,0)
	fwr.write("trigram perplexity = " + str(prplex(ll, _3Count )))
	fwr.write("\n")
	ll = _4grams(sent,0)
	fwr.write("4gram perplexity   = " + str(prplex(ll, _4Count )))
	fwr.write("\n")
	ll = _5grams(sent,0)
	fwr.write("5gram perplexity   = " + str(prplex(ll, _5Count )))
	fwr.write("\n")
	sent = "<s>आकाश_N_NN में_PSP भीषण_JJ विस्फोट_N_NN जैसी_N_NN ध्वनि_N_NN के_PSP साथ_PSP हजार_N_NN सूर्यों_N_NN का_PSP उजाला_N_NN फैलता_V_VM देख_V_VM कर_V_VAUX सब_QT चौंक_N_NN गए_V_VM </s>"
	fwr.write(sent+"\n")
	ll = bigrams(sent, 0)
	fwr.write("Bigram perplexity  = " + str(prplex(ll,bigramCount)))
	fwr.write("\n")
	ll = trigrams(sent,0)
	fwr.write("trigram perplexity = " + str(prplex(ll, _3Count )))
	fwr.write("\n")
	ll = _4grams(sent,0)
	fwr.write("4gram perplexity   = " + str(prplex(ll, _4Count )))
	fwr.write("\n")
	ll = _5grams(sent,0)
	fwr.write("5gram perplexity   = " + str(prplex(ll, _5Count )))
	fwr.write("\n")
	fwr.close()
if __name__ == "__main__":
	fr = open('Hindi-tagged-18.txt',encoding="utf8")
	fb = open("bigram-output.txt", "w",encoding="utf8")
	f3 = open("tri-output.txt", "w",encoding="utf8")
	f4 = open("4gram-output.txt", "w",encoding="utf8")
	f5 = open("5gram-output.txt", "w",encoding="utf8")

	for sent in fr:
		bb = bigrams(sent,1)
		for i in range(0, len(bb)):
			fb.write(bb[i])
			fb.write("\n")

		bb = trigrams(sent,1)
		for i in range(0, len(bb)):
			f3.write(bb[i])
			f3.write("\n")

		bb = _4grams(sent,1)
		for i in range(0, len(bb)):
			f4.write(bb[i])
			f4.write("\n")

		bb = _5grams(sent,1)
		for i in range(0, len(bb)):
			f5.write(bb[i])
			f5.write("\n")


	print(wordsTagsCountc["<s>"])


	fr.close()	
	fb.close()	
	f3.close()	
	f4.close()	
	f5.close()	
	perplex()
	ttp()
	wep()