import ply.lex as lex
import ply.yacc as yacc
import tkinter as tk
from tkinter import filedialog, messagebox
import time
import os

tokens = ["Doctype", "Aperturaarticle", "Cierrearticle", "Aperturatitle",
"Cierretitle", "Aperturainfo", "Cierreinfo", "Aperturaitemizedlist", "Cierreitemizedlist", "Aperturaimportant", "Cierreimportant", "Aperturapara",
"Cierrepara", "Aperturaaddress", "Cierreaddress", "Aperturamediaobject", "Cierremediaobject", "Aperturacomment", "Cierrecomment", "Aperturainformaltable",
"Cierreinformaltable", "Aperturaabstract", "Cierreabstract", "Aperturastreet", "Cierrestreet", "Aperturaphone", "Cierrephone", "Aperturayear","Cierreyear","Aperturaholder","Cierreholder","Aperturasection", "Cierresection", "Aperturasimplesect", 
"Cierresimplesect", "Aperturaauthor", "Cierreauthor", "Aperturadate", "Cierredate", "Aperturacopyright", "Cierrecopyright", "Aperturacity", "Cierrecity", 
"Aperturastate", "Cierrestate", "Aperturaemail", "Cierreemail", "Aperturafirstname", "Cierrefirstname", "Aperturasurname", "Cierresurname", "Aperturaemphasis", 
"Cierreemphasis","Aperturasimpara", "Cierresimpara", "Aperturavideoobject", "Cierrevideoobject", "Aperturaimageobject", "Cierreimageobject", "Aperturalistitem", 
"Cierrelistitem","Aperturatgroup", "Cierretgroup", "Aperturatbody", "Cierretbody", "Aperturatfoot", "Cierretfoot", "Aperturathead", "Cierrethead", "Aperturarow", 
"Cierrerow", "Aperturaentry", "Cierreentry","Aperturaentrytbl", "Cierreentrytbl", "Aperturalink", "Cierrelink", "videodata", "imagedata", "texto"]

linkob = []
aperturas = []

t_Aperturaarticle = r"<article>"
t_Cierrearticle = r"</article>"
t_Cierretitle = r"</title>"
t_Cierreimportant = r"</important>"
t_Cierrepara = r"</para>"
t_Cierreaddress = r"</address>"
t_Cierremediaobject = r"</mediaobject>"
t_Aperturacomment = r"<comment>"
t_Cierrecomment = r"</comment>"
t_Aperturainformaltable = r"<informaltable>"
t_Cierreinformaltable = r"</informaltable>"
t_Cierreabstract = r"</abstract>"
t_Aperturastreet = r"<street>"
t_Cierrestreet = r"</street>"
t_Aperturaphone = r"<phone>"
t_Cierrephone = r"</phone>"
t_Aperturayear = r"<year>"
t_Cierreyear = r"</year>"
t_Aperturaholder = r"<holder>"
t_Cierreholder = r"</holder>"
t_Cierreauthor = r"</author>"
t_Cierredate = r"</date>"
t_Cierrecopyright = r"</copyright>"
t_Aperturacity = r"<city>"
t_Cierrecity = r"</city>"
t_Aperturastate = r"<state>"
t_Cierrestate = r"</state>"
t_Aperturaemail = r"<email>"
t_Cierreemail = r"</email>"
t_Aperturafirstname = r"<firstname>"
t_Cierrefirstname = r"</firstname>"
t_Aperturasurname = r"<surname>"
t_Cierresurname = r"</surname>"
t_Aperturaemphasis = r"<emphasis>"
t_Cierreemphasis = r"</emphasis>"
t_Cierresimpara = r"</simpara>"
t_Aperturavideoobject = r"<videoobject>"
t_Cierrevideoobject = r"</videoobject>"
t_Aperturaimageobject = r"<imageobject>"
t_Cierreimageobject = r"</imageobject>"
t_Cierretgroup = r"</tgroup>"
t_Cierretbody = r"</tbody>"
t_Cierretfoot = r"</tfoot>"
t_Cierrethead = r"</thead>"
t_Cierrerow = r"</row>"
t_Cierreentry = r"</entry>"
t_Cierreentrytbl = r"</entrytbl>"
t_Cierreitemizedlist = r"</itemizedlist>"
t_Cierrelistitem = r"</listitem>"
t_videodata = r"<videodata[ ]fileref=([a-zA-Z]+/)*[a-zA-Z]+.[a-zA-Z]+/>"
t_imagedata = r"<imagedata[ ]fileref=([a-zA-Z]+/)*[a-zA-Z]+.[a-zA-Z]+/>"
t_ignore  = " \t"
t_texto = r'[^<>]+'
t_Cierrelink = r"</link>"

def t_Aperturalink(t):
    r"<xlink:href=\"(https|http|ftps|ftp)://([a-zA-Z]+\.)?([a-zA-Z]+)+(\.[a-zA-Z]+)*(:[0-9]+)?(/[a-zA-Z]+)*(\#[0-9]+)?\"/>"
    global aperturas
    aperturas.append(f"<a link href={t.value[12: -2]}>")
    return t

def t_Doctype(t):
    r"<!DOCTYPE[ ]article>"
    global aperturas
    aperturas.append("<!DOCTYPE article>")
    return t

def t_Aperturatitle(t):
    r"<title>"
    global aperturas
    if es_info:
        aperturas.append("<p>")
    if es_section:
        aperturas.append("<h2>")
    else:
        aperturas.append("<h1>")
    return t

def t_Aperturapara(t):
    r"<para>"
    global aperturas
    aperturas.append("<p>")
    return t

def t_Aperturasimpara(t):
    r"<simpara>"
    global aperturas
    aperturas.append("<p>")
    return t

def t_Aperturaitemizedlist(t):
    r"<itemizedlist>"
    global aperturas
    aperturas.append("<ul>")
    return t

def t_Aperturalistitem(t):
    r"<listitem>"
    global aperturas
    aperturas.append("<li>")
    return t

def t_Aperturasection(t):
    r"<section>"
    global es_section
    es_section = True
    return t

def t_Cierresection(t):
    r"</section>"
    global es_section
    es_section = False
    return t

def t_Aperturasimplesect(t):
    r"<simplesect>"
    global es_section
    es_section = True
    return t

def t_Cierresimplesect(t):
    r"</simplesect>"
    global es_section
    es_section = False
    return t

def t_Aperturatgroup(t):
    r"<tgroup>"
    global aperturas
    aperturas.append("<table border=\"1\" bordercolor=\"green\">")
    return t

def t_Aperturatbody(t):
    r"<tbody>"
    global aperturas
    aperturas.append("<tbody>")
    return t

def t_Aperturathead(t):
    r"<thead>"
    global aperturas
    aperturas.append("<thead style = background-color:#ABABAB>")
    return t

def t_Aperturatfoot(t):
    r"<tfoot>"
    global aperturas
    aperturas.append("<tfoot style = background-color:#E8E8E8>")
    return t

def t_Aperturarow(t):
    r"<row>"
    global aperturas
    aperturas.append("<tr>")
    return t

def t_Aperturaentry(t):
    r"<entry>"
    global aperturas
    aperturas.append("<th>")
    return t  

def t_Aperturaentrytbl(t):
    r"<entrytbl>"
    global aperturas
    aperturas.append("<th><table border=\"1\" bordercolor=\"blue\">")
    return t  

def t_Aperturainfo(t):
    r"<info>"
    global es_info
    es_info = True
    return t  

def t_Cierreinfo(t):
    r"</info>"
    global es_info
    es_info = False
    return t  

def t_Aperturamediaobject(t):
    r"<mediaobject>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return t

def t_Aperturaaddress(t):
    r"<address>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return(t)

def t_Aperturaabstract(t):
    r"<abstract>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return(t)

def t_Aperturaauthor(t):
    r"<author>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return(t)

def t_Aperturadate(t):
    r"<date>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return(t)

def t_Aperturacopyright(t):
    r"<copyright>"
    if es_info:
        aperturas.append("<p style=\"background-color: green; color: white; font-size: 8pt;\">")
    return(t)

def t_Aperturaimportant(t):
    r"<important>"
    aperturas.append("<strong style=\"background-color: red; color: white;\">")
    return(t)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: {t.value} en {t.lineno}")
    t.lexer.skip(1)

def p_error(p):
    if p is None:
        print("Error: Fin inesperado del archivo")
    else:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno} y columna {obtener_columna(p)}")

def obtener_columna(token):
    última_línea_posición = token.lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - última_línea_posición) + 1

def ap_tok():
    while True:
        if len(aperturas)==0:
            break
        else:
            salida.write(aperturas.pop(0))

def p_sigma(p):
    """sigma : Doctype Aperturaarticle article Cierrearticle
            | Doctype Aperturaarticle etiquetas_article Cierrearticle"""
    p[0] = p[3]

def p_article(p):
    """article : titulo etiquetas_article
            | titulo etiquetas_article section
            | titulo etiquetas_article simplesect
            | etiquetas_article section
            | etiquetas_article simplesect
            | info etiquetas_article section
            | info etiquetas_article
            | info etiquetas_article simplesect
            | info titulo etiquetas_article
            | info titulo etiquetas_article section
            | info titulo etiquetas_article simplesect"""
    if len(p)==3:
        p[0] = (p[1], p[2])
    else:
        p[0] = (p[1], p[2], p[3])

def p_info(p):
    """info : Aperturainfo informacion Cierreinfo"""
    p[0] = p[2]

def p_titulo(p):
    "titulo : Aperturatitle title Cierretitle"
    p[0] = p[2]
    salida.write("</h1>")

def p_titulo_s(p):
    "titulo_s : Aperturatitle title Cierretitle"
    p[0] = p[2]
    salida.write("</h2>")
    
def p_etiquetas_article(p):
    """etiquetas_article : Aperturaimportant important Cierreimportant
                        | Aperturapara para Cierrepara
                        | Aperturasimpara simpara Cierresimpara
                        | Aperturaaddress address Cierreaddress
                        | Aperturamediaobject mediaobject Cierremediaobject
                        | Aperturamediaobject media Cierremediaobject
                        | Aperturainformaltable informaltable Cierreinformaltable
                        | Aperturacomment comment Cierrecomment
                        | Aperturaabstract abstract Cierreabstract
                        | Aperturaabstract tabstract Cierreabstract
                        | Aperturaimportant important Cierreimportant etiquetas_article
                        | Aperturapara para Cierrepara etiquetas_article
                        | Aperturasimpara simpara Cierresimpara etiquetas_article
                        | Aperturaaddress address Cierreaddress etiquetas_article
                        | Aperturamediaobject mediaobject Cierremediaobject etiquetas_article
                        | Aperturamediaobject media Cierremediaobject etiquetas_article
                        | Aperturainformaltable informaltable Cierreinformaltable etiquetas_article
                        | Aperturacomment comment Cierrecomment etiquetas_article
                        | Aperturaabstract abstract Cierreabstract etiquetas_article
                        | Aperturaabstract tabstract Cierreabstract etiquetas_article
                        | nuevalista
                        | nuevalista etiquetas_article"""
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==3:
        p[0] = (p[1], p[2])
    elif len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[2], p[4])
    
def p_section_1(p):
    """section : Aperturasection info titulo_s etiquetas_article section Cierresection
                | Aperturasection info titulo_s etiquetas_article simplesect Cierresection
                | Aperturasection info titulo_s etiquetas_article Cierresection
                | Aperturasection titulo_s etiquetas_article section Cierresection
                | Aperturasection titulo_s etiquetas_article simplesect Cierresection
                | Aperturasection titulo_s etiquetas_article Cierresection
                | Aperturasection info etiquetas_article section Cierresection
                | Aperturasection info etiquetas_article simplesect Cierresection
                | Aperturasection info etiquetas_article Cierresection
                | Aperturasection etiquetas_article section Cierresection
                | Aperturasection etiquetas_article simplesect Cierresection
                | Aperturasection etiquetas_article Cierresection"""
    if len(p)==4:
        p[0] = p[2]
    else:
        if len(p)==5:
            p[0] = (p[2], p[3])
        else:
            p[0] = (p[2], p[3], p[4])

def p_section_2(p):
    """section :  Aperturasection info titulo_s etiquetas_article section Cierresection section
                | Aperturasection info titulo_s etiquetas_article simplesect Cierresection section
                | Aperturasection info titulo_s etiquetas_article Cierresection section
                | Aperturasection titulo_s etiquetas_article section Cierresection section
                | Aperturasection titulo_s etiquetas_article simplesect Cierresection section
                | Aperturasection titulo_s etiquetas_article Cierresection section
                | Aperturasection info etiquetas_article section Cierresection section
                | Aperturasection info etiquetas_article simplesect Cierresection section
                | Aperturasection info etiquetas_article Cierresection section
                | Aperturasection etiquetas_article section Cierresection section
                | Aperturasection etiquetas_article simplesect Cierresection section
                | Aperturasection etiquetas_article Cierresection section
                | Aperturasection info titulo_s etiquetas_article section Cierresection simplesect
                | Aperturasection info titulo_s etiquetas_article simplesect Cierresection simplesect
                | Aperturasection info titulo_s etiquetas_article Cierresection simplesect
                | Aperturasection titulo_s etiquetas_article section Cierresection simplesect
                | Aperturasection titulo_s etiquetas_article simplesect Cierresection simplesect
                | Aperturasection titulo_s etiquetas_article Cierresection simplesect
                | Aperturasection info etiquetas_article section Cierresection simplesect
                | Aperturasection info etiquetas_article simplesect Cierresection simplesect
                | Aperturasection info etiquetas_article Cierresection simplesect
                | Aperturasection etiquetas_article section Cierresection simplesect
                | Aperturasection etiquetas_article simplesect Cierresection simplesect
                | Aperturasection etiquetas_article Cierresection simplesect"""
    if len(p)==5:
        p[0] = (p[2], p[4])
    else:
        if len(p)==6:
            p[0] = (p[2], p[3], p[5])
        else:
            p[0] = (p[2], p[3], p[4], p[6])

def p_simplesect(p):    
    '''simplesect : Aperturasimplesect etiquetas_article Cierresimplesect
                | Aperturasimplesect titulo_s etiquetas_article Cierresimplesect
                | Aperturasimplesect info etiquetas_article Cierresimplesect
                | Aperturasimplesect info titulo_s etiquetas_article Cierresimplesect'''
    if len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[2], p[3])

def p_informacion(p):
    """informacion : Aperturamediaobject mediaobject Cierremediaobject
            | Aperturaabstract abstract Cierreabstract
            | Aperturaabstract tabstract Cierreabstract
            | Aperturaaddress address Cierreaddress
            | Aperturaauthor author Cierreauthor
            | Aperturadate date Cierredate
            | Aperturacopyright copyright Cierrecopyright
            | titulo
            | Aperturamediaobject media Cierremediaobject
            | Aperturamediaobject mediaobject Cierremediaobject informacion
            | Aperturaabstract abstract Cierreabstract informacion
            | Aperturaabstract tabstract Cierreabstract informacion
            | Aperturaaddress address Cierreaddress informacion
            | Aperturaauthor author Cierreauthor informacion
            | Aperturadate date Cierredate informacion
            | Aperturacopyright copyright Cierrecopyright informacion
            | titulo informacion
            | Aperturamediaobject media Cierremediaobject informacion"""
    if len(p)==2:
        p[0] = p[1]
    elif len(p)==3:
        p[0] = (p[1], p[2])
    elif len(p)==4:
        p[0] = (p[2])
    else:
        p[0] = (p[2], p[4])


def p_abstract(p):
    "abstract : titulo tabstract"
    p[0] = (p[1], p[2])
    
def p_tabstract(p):
    """tabstract : Aperturapara para Cierrepara
                | Aperturasimpara simpara Cierresimpara
                | Aperturapara para Cierrepara tabstract
                | Aperturasimpara simpara Cierresimpara tabstract"""
    if len(p)==4:
        p[0] = (p[2])
        if es_info:
            aperturas.append("</p>")
    else:
        p[0] = (p[2], p[4])

def p_address(p):
    """address : texto
            | Aperturastreet street Cierrestreet
            | Aperturacity city Cierrecity
            | Aperturastate state Cierrestate
            | Aperturaphone phone Cierrephone
            | Aperturaemail email Cierreemail
            | texto address
            | Aperturastreet street Cierrestreet address
            | Aperturacity city Cierrecity address
            | Aperturastate state Cierrestate address
            | Aperturaphone phone Cierrephone address
            | Aperturaemail email Cierreemail address"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
        if es_info:
            aperturas.append("</p>")
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
                if es_info:
                    aperturas.append("</p>")
            else:
                p[0] = (p[2], p[4])

def p_author(p):
    """author : Aperturafirstname firstname Cierrefirstname
            | Aperturasurname surname Cierresurname
            | Aperturafirstname firstname Cierrefirstname author
            | Aperturasurname surname Cierresurname author"""
    if len(p)==4:
        p[0] = p[2]
        if es_info:
            aperturas.append("</p>")
    else:
        p[0] = (p[2],p[4])

def p_copyright(p):
    """copyright : Aperturayear year Cierreyear
                | Aperturayear year Cierreyear Aperturaholder holder Cierreholder
                | Aperturayear year Cierreyear copyright
                | Aperturayear year Cierreyear copyright Aperturaholder holder Cierreholder"""
    if len(p)==4:
        p[0] = p[2]
        if es_info:
            aperturas.append("</p>")
    else:
        if len(p)==5:
            p[0] = (p[2],p[4])
        else:
            if len(p)==7:
                p[0] = (p[2], p[5])
                if es_info:
                    aperturas.append("</p>")
            else:
                p[0] = (p[2], p[4], p[6])

def p_title(p):
    """title : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturalink link Cierrelink
            | Aperturaemail email Cierreemail
            | texto title
            | Aperturaemphasis emphasis Cierreemphasis title
            | Aperturalink link Cierrelink title
            | Aperturaemail email Cierreemail title"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])


def p_simpara(p):
    """simpara : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturalink link Cierrelink
            | Aperturaemail email Cierreemail
            | Aperturaauthor author Cierreauthor
            | Aperturacomment comment Cierrecomment
            | texto simpara
            | Aperturaemphasis emphasis Cierreemphasis simpara
            | Aperturalink link Cierrelink simpara
            | Aperturaemail email Cierreemail simpara
            | Aperturaauthor author Cierreauthor simpara
            | Aperturacomment comment Cierrecomment simpara"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_emphasis(p):
    """emphasis : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturalink link Cierrelink
            | Aperturaemail email Cierreemail
            | Aperturaauthor author Cierreauthor
            | Aperturacomment comment Cierrecomment
            | texto emphasis
            | Aperturaemphasis emphasis Cierreemphasis emphasis
            | Aperturalink link Cierrelink emphasis
            | Aperturaemail email Cierreemail emphasis
            | Aperturaauthor author Cierreauthor emphasis
            | Aperturacomment comment Cierrecomment emphasis"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_comment(p):
    """comment : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturalink link Cierrelink
            | Aperturaemail email Cierreemail
            | Aperturaauthor author Cierreauthor
            | Aperturacomment comment Cierrecomment
            | texto comment
            | Aperturaemphasis emphasis Cierreemphasis comment
            | Aperturalink link Cierrelink comment
            | Aperturaemail email Cierreemail comment
            | Aperturaauthor author Cierreauthor comment
            | Aperturacomment comment Cierrecomment comment"""
    if len(p)==2:
        p[0] = p[1]
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = (p[1],p[2])
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_link(p):
    """link : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturalink link Cierrelink
            | Aperturaemail email Cierreemail
            | Aperturaauthor author Cierreauthor
            | Aperturacomment comment Cierrecomment
            | texto link
            | Aperturaemphasis emphasis Cierreemphasis link
            | Aperturalink link Cierrelink link
            | Aperturaemail email Cierreemail link
            | Aperturaauthor author Cierreauthor link
            | Aperturacomment comment Cierrecomment link"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
        salida.write("</a>")

    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
                salida.write("</a>")
            else:
                p[0] = (p[2], p[4])
    
    

def p_para(p):
    """para : texto
        | Aperturaemphasis emphasis Cierreemphasis
        | Aperturalink link Cierrelink
        | Aperturaemail email Cierreemail
        | Aperturaauthor author Cierreauthor
        | Aperturacomment comment Cierrecomment
        | Aperturaimportant important Cierreimportant
        | Aperturaaddress address Cierreaddress
        | Aperturamediaobject mediaobject Cierremediaobject
        | Aperturainformaltable informaltable Cierreinformaltable
        | Aperturamediaobject media Cierremediaobject
        | texto para
        | Aperturaemphasis emphasis Cierreemphasis para
        | Aperturalink link Cierrelink para
        | Aperturaemail email Cierreemail para
        | Aperturaauthor author Cierreauthor para
        | Aperturacomment comment Cierrecomment para
        | Aperturaimportant important Cierreimportant para
        | Aperturaaddress address Cierreaddress para
        | Aperturamediaobject mediaobject Cierremediaobject para
        | Aperturainformaltable informaltable Cierreinformaltable para
        | Aperturamediaobject media Cierremediaobject para"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
        salida.write(" </p>")
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
                salida.write(" </p>")
            else:
                p[0] = (p[2], p[4])

def p_para_2(p):
    """para : nuevalista
            | nuevalista para"""
    if len(p)==2:
        p[0] = p[1]
        salida.write(" </p>")
    else:
        p[0] = (p[1], p[2])    

def p_important(p):
    """important : nuevalista
                | Aperturaimportant important Cierreimportant
                | Aperturapara para Cierrepara
                | Aperturasimpara simpara Cierresimpara
                | Aperturaaddress address Cierreaddress
                | Aperturamediaobject mediaobject Cierremediaobject
                | Aperturainformaltable informaltable Cierreinformaltable
                | Aperturacomment comment Cierrecomment
                | Aperturaabstract abstract Cierreabstract
                | Aperturaabstract tabstract Cierreabstract
                | Aperturamediaobject media Cierremediaobject
                | nuevalista important
                | Aperturaimportant important Cierreimportant important
                | Aperturapara para Cierrepara important
                | Aperturasimpara simpara Cierresimpara important
                | Aperturaaddress address Cierreaddress important
                | Aperturamediaobject mediaobject Cierremediaobject important
                | Aperturainformaltable informaltable Cierreinformaltable important
                | Aperturacomment comment Cierrecomment important
                | Aperturaabstract abstract Cierreabstract important
                | Aperturaabstract tabstract Cierreabstract important
                | Aperturamediaobject media Cierremediaobject important"""
    if len(p)==2:
        p[0] = p[1]
        salida.write("</strong>")
    elif len(p)==3:
        p[0] = (p[1], p[2])
    elif len(p)==4:
        p[0] = p[2]
        salida.write("</strong>")
    else:
        p[0] = (p[2],p[4])

def p_important_t(p):
    """important : Aperturatitle title Cierretitle nuevalista
                | Aperturatitle title Cierretitle Aperturaimportant important Cierreimportant
                | Aperturatitle title Cierretitle Aperturapara para Cierrepara
                | Aperturatitle title Cierretitle Aperturasimpara simpara Cierresimpara
                | Aperturatitle title Cierretitle Aperturaaddress address Cierreaddress
                | Aperturatitle title Cierretitle Aperturamediaobject mediaobject Cierremediaobject
                | Aperturatitle title Cierretitle Aperturainformaltable informaltable Cierreinformaltable
                | Aperturatitle title Cierretitle Aperturacomment comment Cierrecomment
                | Aperturatitle title Cierretitle Aperturaabstract abstract Cierreabstract
                | Aperturatitle title Cierretitle Aperturaabstract tabstract Cierreabstract
                | Aperturatitle title Cierretitle Aperturamediaobject media Cierremediaobject
                | Aperturatitle title Cierretitle nuevalista important
                | Aperturatitle title Cierretitle Aperturaimportant important Cierreimportant important
                | Aperturatitle title Cierretitle Aperturapara para Cierrepara important
                | Aperturatitle title Cierretitle Aperturasimpara simpara Cierresimpara important
                | Aperturatitle title Cierretitle Aperturaaddress address Cierreaddress important
                | Aperturatitle title Cierretitle Aperturamediaobject mediaobject Cierremediaobject important
                | Aperturatitle title Cierretitle Aperturainformaltable informaltable Cierreinformaltable important
                | Aperturatitle title Cierretitle Aperturacomment comment Cierrecomment important
                | Aperturatitle title Cierretitle Aperturaabstract abstract Cierreabstract important
                | Aperturatitle title Cierretitle Aperturaabstract tabstract Cierreabstract important
                | Aperturatitle title Cierretitle Aperturamediaobject media Cierremediaobject important"""
    if len(p)==5:
        p[0] = (p[2], p[4])
        salida.write("</h1>")
        salida.write("</strong>")
    elif len(p)==6:
        p[0] = (p[2], p[3], p[4])
    elif len(p)==7:
        p[0] = (p[2], p[5])
        salida.write("</h1>")
        salida.write("</strong>")
    else:
        p[0] = (p[2], p[5], p[7])

def p_firstname(p):
    """firstname : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto firstname
                | Aperturaemphasis emphasis Cierreemphasis firstname
                | Aperturacomment comment Cierrecomment firstname
                | Aperturalink link Cierrelink firstname"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_surname(p):
    """surname : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto surname
                | Aperturaemphasis emphasis Cierreemphasis surname
                | Aperturacomment comment Cierrecomment surname
                | Aperturalink link Cierrelink surname"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_street(p):
    """street : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto street
                | Aperturaemphasis emphasis Cierreemphasis street
                | Aperturacomment comment Cierrecomment street
                | Aperturalink link Cierrelink street"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_city(p):
    """city : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto city
                | Aperturaemphasis emphasis Cierreemphasis city
                | Aperturacomment comment Cierrecomment city
                | Aperturalink link Cierrelink city"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_state(p):
    """state : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto state
                | Aperturaemphasis emphasis Cierreemphasis state
                | Aperturacomment comment Cierrecomment state
                | Aperturalink link Cierrelink state"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_phone(p):
    """phone : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto phone
                | Aperturaemphasis emphasis Cierreemphasis phone
                | Aperturacomment comment Cierrecomment phone
                | Aperturalink link Cierrelink phone"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_email(p):
    """email : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto email
                | Aperturaemphasis emphasis Cierreemphasis email
                | Aperturacomment comment Cierrecomment email
                | Aperturalink link Cierrelink email"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_date(p):
    """date : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto date
                | Aperturaemphasis emphasis Cierreemphasis date
                | Aperturacomment comment Cierrecomment date
                | Aperturalink link Cierrelink date"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
        if es_info:
            aperturas.append("</p>")
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
                if es_info:
                    aperturas.append("</p>")
            else:
                p[0] = (p[2], p[4])

def p_year(p):
    """year : texto
                | Aperturaemphasis emphasis Cierreemphasis
                | Aperturacomment comment Cierrecomment
                | Aperturalink link Cierrelink
                | texto year
                | Aperturaemphasis emphasis Cierreemphasis year
                | Aperturacomment comment Cierrecomment year
                | Aperturalink link Cierrelink year"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_holder(p):
    """holder : texto
            | Aperturaemphasis emphasis Cierreemphasis
            | Aperturacomment comment Cierrecomment
            | Aperturalink link Cierrelink
            | texto holder
            | Aperturaemphasis emphasis Cierreemphasis holder
            | Aperturacomment comment Cierrecomment holder
            | Aperturalink link Cierrelink holder"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
    else:
        if len(p)==3:
            p[0] = p[2]
            ap_tok()
            salida.write(p[1])
        else:
            if len(p)==4:
                p[0] = p[2]
            else:
                p[0] = (p[2], p[4])

def p_mediaobject(p):
    "mediaobject : Aperturainfo informacion Cierreinfo media"
    p[0] = (p[2], p[4])
    if es_info:
            aperturas.append("</p>")

def p_media(p):
    """media : Aperturavideoobject videoobject Cierrevideoobject
            | Aperturaimageobject imageobject Cierreimageobject
            | Aperturavideoobject videoobject Cierrevideoobject media
            | Aperturaimageobject imageobject Cierreimageobject media"""
    if len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[2], p[4])

def p_videoobject(p):
    """videoobject : videodata
                | Aperturainfo informacion Cierreinfo videodata"""
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[4])

def p_imageobject(p):
    """imageobject : imagedata
                | Aperturainfo informacion Cierreinfo imagedata"""
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[4])

def p_nuevalista(p):
    """nuevalista : Aperturaitemizedlist itemizedlist Cierreitemizedlist"""
    p[0] = p[2]
    salida.write("</ul>")

def p_itemizedlist(p):
    """itemizedlist : Aperturalistitem listitem Cierrelistitem
                | Aperturalistitem listitem Cierrelistitem itemizedlist"""
    if len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[1], p[3])
        

def p_listitem(p):
    """listitem : Aperturaimportant important Cierreimportant
            | Aperturapara para Cierrepara
            | Aperturasimpara simpara Cierresimpara
            | Aperturaaddress address Cierreaddress
            | Aperturamediaobject mediaobject Cierremediaobject
            | Aperturainformaltable informaltable Cierreinformaltable
            | Aperturacomment comment Cierrecomment
            | Aperturaabstract abstract Cierreabstract
            | Aperturaabstract tabstract Cierreabstract
            | Aperturamediaobject media Cierremediaobject
            | Aperturaimportant important Cierreimportant listitem
            | Aperturapara para Cierrepara listitem
            | Aperturasimpara simpara Cierresimpara listitem
            | Aperturaaddress address Cierreaddress listitem
            | Aperturamediaobject mediaobject Cierremediaobject listitem
            | Aperturainformaltable informaltable Cierreinformaltable listitem
            | Aperturacomment comment Cierrecomment listitem
            | Aperturaabstract abstract Cierreabstract listitem
            | Aperturaabstract tabstract Cierreabstract listitem
            | Aperturamediaobject media Cierremediaobject listitem
            | nuevalista
            | nuevalista listitem"""
    if len(p)==2:
        p[0] = p[1]
        salida.write("</li>")
    elif len(p)==3:
        p[0] = (p[1], p[2])
    elif len(p)==4:
        p[0] = p[2]
        salida.write("</li>")
    else:
        p[0] = (p[2], p[4])

def p_informaltable(p):
    """informaltable : Aperturamediaobject mediaobject Cierremediaobject
                    | Aperturamediaobject media Cierremediaobject
                    | Aperturatgroup tgroup Cierretgroup
                    | Aperturamediaobject mediaobject Cierremediaobject informaltable
                    | Aperturamediaobject media Cierremediaobject informaltable
                    | Aperturatgroup tgroup Cierretgroup informaltable"""
    if len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[2], p[4])

def p_tgroup(p):
    """tgroup : Aperturatbody tbody Cierretbody
            | Aperturatfoot tfoot Cierretfoot Aperturatbody tbody Cierretbody
            | Aperturathead thead Cierrethead Aperturatbody tbody Cierretbody
            | Aperturathead thead Cierrethead Aperturatfoot tfoot Cierretfoot Aperturatbody tbody Cierretbody"""
    if len(p)==4:
        p[0] = p[2]
    else:
        if len(p)==7:
            p[0] = (p[2], p[5])
        else:
            p[0] = (p[2], p[5], p[8])
    salida.write("</table>\n")

def p_thead(p):
    """thead : Aperturarow row Cierrerow
            | Aperturarow row Cierrerow thead"""
    if len(p)==4:
        p[0] = p[2]
        salida.write("</thead>\n")
    else:
        p[0] = (p[2],p[4])

def p_tfoot(p):
    """tfoot : Aperturarow row Cierrerow
            | Aperturarow row Cierrerow tfoot"""
    if len(p)==4:
        p[0] = p[2]
        salida.write("</tfoot>\n")
    else:
        p[0] = (p[2],p[4])

def p_tbody(p):
    """tbody : Aperturarow row Cierrerow
            | Aperturarow row Cierrerow tbody"""
    if len(p)==4:
        p[0] = p[2]
        salida.write("</tbody>\n")
    else:
        p[0] = (p[2],p[4])

def p_row(p):
    """row : Aperturaentry entry Cierreentry
        | Aperturaentrytbl entrytbl Cierreentrytbl
        | Aperturaentry entry Cierreentry row
        | Aperturaentrytbl entrytbl Cierreentrytbl row"""
    if len(p)==4:
        p[0] = p[2]
        salida.write("</tr>\n")
    else:
        p[0] = (p[2], p[4])

def p_entrytbl(p):
    """entrytbl : Aperturathead thead Cierrethead Aperturatbody tbody Cierretbody
            | Aperturatbody tbody Cierretbody"""
    if len(p)==4:
        p[0] = p[2]
    else:
        p[0] = (p[2], p[5])
    salida.write("</table></th>\n")

def p_entry(p):
    """entry : texto
            | nuevalista
            | Aperturaimportant important Cierreimportant
            | Aperturapara para Cierrepara
            | Aperturasimpara simpara Cierresimpara
            | Aperturamediaobject mediaobject Cierremediaobject
            | Aperturamediaobject media Cierremediaobject
            | Aperturacomment comment Cierrecomment
            | Aperturaabstract abstract Cierreabstract
            | Aperturaabstract tabstract Cierreabstract
            | texto entry
            | nuevalista entry
            | Aperturaimportant important Cierreimportant entry
            | Aperturapara para Cierrepara entry
            | Aperturasimpara simpara Cierresimpara entry
            | Aperturamediaobject mediaobject Cierremediaobject entry
            | Aperturamediaobject media Cierremediaobject entry
            | Aperturacomment comment Cierrecomment entry
            | Aperturaabstract abstract Cierreabstract entry
            | Aperturaabstract tabstract Cierreabstract entry"""
    if len(p)==2:
        ap_tok()
        salida.write(p[1])
        salida.write("</th>\n")
        p[0] = p[1]
    else:
        if len(p)==3:
            p[0] = (p[1],p[2])
        else:
            if len(p)==4:
                p[0] = p[2]
                salida.write("</th>\n")
            else:
                p[0] = (p[2], p[4])
        

parser = yacc.yacc()
lexer = lex.lex()
string = ""
current_file = os.path.abspath(__file__)
es_section = False
es_info = False

def analyze_file():
    global salida
    file_path = filedialog.askopenfilename(filetypes=[("XML Files", "*.xml")])
    print(file_path)
    if file_path:
        salida = open(os.path.join(os.path.dirname(current_file), (os.path.basename(file_path)).replace(".xml", ".html")), "w")
        try:
            with open(file_path, 'r') as file:
                input_text.delete(1.0, tk.END)  # Eliminar el contenido actual del widget de texto
                input_text.insert(tk.END, file.read())  # Insertar el contenido del archivo en el widget de texto
                parse_input(input_text.get("1.0", tk.END))
        except:
            messagebox.showerror("Error", "Error al leer el archivo XML")
    else:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo")

def parse_input(input_string):
    global salida
    result = parser.parse(input_string, lexer=lexer)
    if result is not None:
        output_text.configure(text="El texto es sintácticamente válido.")
    else:
        output_text.configure(text="El texto no es sintácticamente válido.")
    salida.close()

def analyze_input():
    global salida
    salida = open(os.path.join(os.path.dirname(current_file), "salida.html"), "w")
    input_string = input_text.get("1.0", tk.END)
    parse_input(input_string)
    salida.close()

window = tk.Tk()
window.geometry("800x500")
input_text = tk.Text(window)
input_text.pack()
analyze_button = tk.Button(window, text="Abrir y Analizar", command=analyze_file)
analyze_button.pack()
analyze_input_button = tk.Button(window, text="Analizar Entrada", command=analyze_input)
analyze_input_button.pack()
output_text = tk.Label(window)
output_text.pack()
window.mainloop()
