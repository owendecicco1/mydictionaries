infile = open("info_security.txt","r")
outfile = open("encrypted.txt","w")

encrypted = dict(a="!",A="@",b="#",B="%",c="^",C="&",d="*",D="(",e="-",E="_",f="+",F="=",g="`",G="~",h="{",H="[",i="}",I="]",j="|",J=";",k=";",K=":",l="'",L="<",m=",",M=">",n=".",N="?",o="1",O="2",p="3",P="4",q="5",Q="6",r="7",R="8",s="9",S="10",t="11",T="12",u="13",U="14",v="15",V="16",w="17",W="18",x="19",X="20",y="21",Y="22",z="23",Z="24")
read_file = infile.read()

for characters in read_file:
    if characters in encrypted:
        outfile.write(encrypted[characters])
    else:
        outfile.write(characters)

infile.close()
outfile.close()