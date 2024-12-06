#1)Bir aracın yakıt tipine göre (benzin, dizel, lpg)nbelirtilen bir mesafede ne kadar yakıt masrafı olduğununhesaplayan uygulamayı yapınız.
#benzin=39.35
#dizel=41.71
#lpg=20.28

benzin=39.35
dizel=41.71
lpg=20.28

yakıtTipi=input("Yakıt tipiniz nedir?")
mesafe=int(input("Aldığınız mesafe nedir?"))

if(yakıtTipi=="benzin"):
    print(mesafe*benzin)
elif(yakıtTipi=="dizel"):
    print(mesafe*dizel)
elif(yakıtTipi=="lpg"):
    print(mesafe*lpg)
else:
    print("Üzgünüz, bir sorun oluştu.")



#2)Bir öğrencinin 2 vize 1 final notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen harf notunu yazdırınız.
#90-100 => AA
#80-89 => BA
#70-79 => BB
#60-69 => CB
#50-59 => CC
#40-49 => DC

vize1=int(input("1. vize notunuz nedir?"))
vize2=int(input("2. vize notunuz nedir?"))
final=int(input("Final notunuz nedir?"))

notOrtalaması=(vize1*0.2+vize2*0.2+final*0.6)

if(100>=notOrtalaması>=90):
    print("AA")
elif(89>=notOrtalaması>=80):
    print("BA")
elif(79>=notOrtalaması>=70):
    print("BB")
elif(69>=notOrtalaması>=60):
    print("CB")
elif(59>=notOrtalaması>=50):
    print("CC")
elif(49>=notOrtalaması>=40):
    print("DC")
else:
    print("DD")
