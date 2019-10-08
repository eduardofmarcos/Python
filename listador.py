lista ='''&lt;contatojmimobiliaria@gmail.com&gt;, &quot;condominioadm@imobiliariapilar.com&quot;
&lt;condominioadm@imobiliariapilar.com&gt;, &quot;zanettacristiano@gmail.com&quot;
&lt;zanettacristiano@gmail.com&gt;, &quot;contato@hawzi.com&quot; &lt;contato@hawzi.com&gt;,
&quot;corretorlaguna@gmail.com&quot; &lt;corretorlaguna@gmail.com&gt;,
&quot;isoliveiraimoveis@gmail.com&quot; &lt;isoliveiraimoveis@gmail.com&gt;'''
listasemi = []

for l in lista:
    if l ==',':
        li = lista.split()
#print(li)

for index in range(0,len(li)):
    if index % 2 == 0:
        listasemilimpa = li[index]
        listasemi.append(listasemilimpa)
#print(listasemi)

for email in listasemi:
    if email in lista != 'contato@hawzi.com&gt':
        print(email[4:-2])





#for email in li:
  #  print(email)