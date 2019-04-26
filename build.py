#!/usr/bin/python

import os
import re

lista = []
i = 0
os.system('mkdir TEMP')
os.system('find . -name \*_WM.png\* -type f -delete')
os.system('find . -name \*_WM2.png\* -type f -delete')
os.system('find . -name \*_WM_INFO.png\* -type f -delete')
os.system('rm ./OUT/* > /dev/null 1> /dev/null 2> /dev/null')

for path, subdirs, files in os.walk('.'):
    for name in files:
	plik = os.path.join(path, name)
	
	if len(plik.split('/')) == 4:
	    if plik.find('errc.png') != -1:
		lista.append(plik)


lista.sort()


def prepare(x, elements):
    global i

    temp = x.split('/')
    desc = temp[2].replace('_', ' ')
    x = x.replace('(', '\(').replace(')', '\)')
    src = x
    dst = src+"_WM.png"
    dst2 = src+"_WM2.png"
    dst_info = src+"_WM_INFO.png"
    
    print x
    infofile = './'+temp[1]+'/'+temp[2]+'.html'
    infofile = open(infofile, 'r')
    info = ""
    for txt in infofile:
	if txt.find('<td>BIS</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nBIS\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>LDC</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nLDC\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>PIE</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nPIE\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>PI8</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nPI8\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>PIF</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nPIF\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>BLER</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nBLER\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>E22</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nE22\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>E32</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nE32\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]+'\n'
	
	elif txt.find('<td>UNCR</td>') != -1:
	    r = re.findall(r'.*?>(\d.*?)<', txt)
	    info +="\nUNCR\n"+r[0]+'\nMAX: '+r[1]+'\nAVG: '+r[2]



    infofile.close()

    i += 1

    os.system('convert -size 1900x650 -border 50x0 -background none -bordercolor none -pointsize 40 -fill black -gravity northwest -kerning 2 caption:"'+desc+'" '+dst)
    os.system('convert -size 1850x650 -border 0x0 -bordercolor none -background none -pointsize 40 -fill red -gravity northeast -kerning 2 caption:"'+str(i)+'/'+str(elements)+'" '+dst2)
    os.system('convert -size 1900x650 -border 1785x120 -bordercolor none -background none -pointsize 15 -fill black -gravity northwest -kerning 2 caption:"'+info+'" '+dst_info)
    
    os.system('convert -background white -gravity southwest -extent 1900x650 '+x+' ./TEMP/'+str(i)+'.png')
    os.system('composite -dissolve 50% -tile '+dst+' ./TEMP/'+str(i)+'.png ./TEMP/'+str(i)+'.png')
    os.system('composite -dissolve 50% -tile '+dst2+' ./TEMP/'+str(i)+'.png ./TEMP/'+str(i)+'.png')
    os.system('composite -dissolve 100% -tile '+dst_info+' ./TEMP/'+str(i)+'.png ./TEMP/'+str(i)+'.png')
    os.system("cp ./TEMP/"+str(i)+".png ./OUT/"+l[1].replace('#','_')+'_'+str(i)+'.png')

    plik_details = './OUT/'+l[1].replace('#','_')+'.html'
    linia = '<CENTER><A HREF="'+l[1].replace('#','_')+'_'+str(i)+'.png" TARGET="_blank"><IMG WIDTH="75%" SRC="'+l[1].replace('#','_')+'_'+str(i)+'.png"</IMG></A></CENTER><BR><BR>'
	
    plik_details = open(plik_details, "a+")
    plik_details.write(linia+"\n")
    plik_details.close()


def make(x):
    global i

    print "-----"
    dest = x+'.gif'
    out = './OUT/'+dest

    os.system('convert -delay 200 -loop 0 ./TEMP/*.png '+out.replace('#','_'))

    os.system('rm ./TEMP/*  > /dev/null 1> /dev/null 2> /dev/null')
    
    i = 0

html = "<HTML><BODY>"

old = ""
for x in lista:
    l = x.split('/')
    elements = 0
    for y in lista:
	if (y.find(l[1]) != -1):
	    elements += 1

    if (old != l[1]):
	if old != "":
	    make(old)
	if os.path.isfile("./"+l[1]+"/01.jpg"):
	    os.system("cp ./"+l[1]+"/01.jpg ./OUT/"+l[1].replace('#','_')+"_01.jpg")
	else:
	    os.system("cp ./blank.jpg ./OUT/"+l[1].replace('#','_')+"_01.jpg")
	if os.path.isfile("./"+l[1]+"/02.jpg"):
	    os.system("cp ./"+l[1]+"/02.jpg ./OUT/"+l[1].replace('#','_')+"_02.jpg")
	else:
	    os.system("cp ./blank.jpg ./OUT/"+l[1].replace('#','_')+"_02.jpg")
	if os.path.isfile("./"+l[1]+"/03.jpg"):
	    os.system("cp ./"+l[1]+"/03.jpg ./OUT/"+l[1].replace('#','_')+"_03.jpg")
	else:
	    os.system("cp ./blank.jpg ./OUT/"+l[1].replace('#','_')+"_03.jpg")
	info = './'+l[1]+'/info.html'
	html += '<hr>'
	html += '<DIV style="text-align:left;padding:15px;border:1px dashed black;margin:30px;">'

	info_file = open(info,'r')
	for txt in info_file:
	    txt = txt.replace('01.jpg', (l[1].replace('#', '_')+'_'+'01.jpg'))
	    txt = txt.replace('02.jpg', (l[1].replace('#', '_')+'_'+'02.jpg'))
	    txt = txt.replace('03.jpg', (l[1].replace('#', '_')+'_'+'03.jpg'))
	    html += txt
	info_file.close()
	html += '</DIV>'
	
	html+='<DIV><CENTER><A HREF="'+l[1].replace('#', '_')+'.gif" TARGET="_blank"><IMG WIDTH="75%" SRC="'+l[1].replace('#', '_')+'.gif"></IMG></A></CENTER></DIV>'

	details = l[1].replace('#', '_')+'.html'
	html+= '<div><center><a href="'+details+'"><input type="button" value="Details"/></a></center></div>'



    old = l[1]
    prepare(x, elements)



make(old)

html += "</BODY></HTML>"

plik = open("./OUT/index.html", "w")
plik.write(html)
plik.close()

