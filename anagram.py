def verify_anagrams(first_word, second_word):
    
    def vyhodMedzery(retazec):
    	slovo_list = []
	for char in retazec.lower():
            if 'a' <= char <= 'z':
                slovo_list.append(char)
        return "".join(slovo_list)
	
    if list(vyhodMedzery(first_word)).sort == list(vyhodMedzery(second_word)).sort:
        return True
    else:
        return False
            
    #return True or False

verify_anagrams("Programming", "Gram Ring Mop")
