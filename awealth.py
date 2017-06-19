def mesacny_vynos(rocny_vynos):
	vysledok = ((1 + rocny_vynos)**(1/12)) - 1
	return vysledok

#a = mesacny_vynos(0.07)

def zhodnotenie(suma, pocet_mesiacov, mesacne):
	prispevky = []
	for a in range(1, pocet_mesiacov+1):
		#print(a)
		prispevky.append(round(suma*(1+mesacne)**a,4))
	#print(prispevky)
	return prispevky
	
jon = sum(zhodnotenie(500, 30*12, mesacny_vynos(0.05)))
print(jon)
print((jon*(1+0.07)**30))

#print(500*(1+mesacny_vynos(0.07)))
