# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:35:07 2021

@author: Shun

https://qiita.com/R_olldIce/items/3e2c80baa6d5e6f3abe9#1-pow_mod
"""
import sympy as sp
#import itertools

       
#def calculate(P,C,A,A_inverse)
def main():           
    try:
        mod = 95 #int(input("mod="))
        a = "平文P"#mode調整
        b = "暗号文C"
        
        judge = int(input("以前or持っている暗号化鍵を利用するなら:2\n以前or持っている復号化鍵を利用するなら:1\n以外なら:0 \n judge:"))
        if judge == 2:
            print("基本２次元配列のため\trow=n,column=2と記載する")
            A = key_P_C_insert()
            A_inverse = A.inv_mod(mod)  
        elif judge == 1:
            print("基本２次元配列のため\trow=n,column=2と記載する")
            A_inverse = key_P_C_insert()
            A = A_inverse.inv_mod(mod)
        elif judge == 0:
            A,A_inverse = key(mod)
        else:
            raise ValueError
        
        C,P,P_C_len= None,None,None
        while(1):
                mode = (int(input("鍵閲覧:1,暗号化:2,復号化:3,終了:4 \n input:")))
                if mode == 1:
                    print(F"A≡{A}mod{mod} \nA^-1≡{A_inverse}mod{mod}")
                elif mode == 2 :
                    P,P_C_len= insert_chr(a,P,P_C_len)#(a,Pはどちらでも)
                    C = (A*P)%mod#P
                    print(F"C≡{C}\nmod{mod}")
                    C= int_to_char(C)
                    print(F"C:{C}\nmod{mod}")
                    
                elif mode == 3 :
                    
                    #C = char_to_int(C)
                    C,P_C_len = insert_chr(b,C,P_C_len)
                    P = (A_inverse*C) % mod#C
                    print(F"P≡{P}\nmod{mod}")
                    P = int_to_char(P)
                    print(F"P:{P}\nmod{mod}")
                    if P_C_len % 2 != 0:
                        P = P.strip()
                elif mode == 4 :
                    break
                else:
                    raise ValueError
      
    except  ValueError:
            print("入力値が不正です ")


def insert_chr(mode,P_C,P_C_len)->chr:
    #row,column = 0
    function = int(input(F"{mode}を持っている:1{mode}を持っていない:0 \n function:"))
    try:
        
        if  function == 1:
            if P_C == None:
                P_C = key_P_C_insert()
                P_C_len = int(input("文字数を入力してください \n文字数:"))
            else:
                P_C = char_to_int(P_C)#P_C_lenは前段階で保存されているので大丈夫
        elif function == 0:
            P_C = (input("文字列を入力　95種類　大文字　小文字　数字 etc \n>>"))#A　便宜上
            P_C_judge = int(input("文字数を入力します。外部からの確認用:1,内部:0\n>>"))
            if P_C_judge == 0:
                P_C_len = len(P_C)
            elif P_C_judge == 1:
                P_C_len = int(input("文字数を入力してください \n文字数:"))
            else:
                raise ValueError
            
            P_C= char_to_int(P_C)
            #入力　文字列
        else:#他は考慮しない
            raise ValueError 
    except  ValueError:
        print("入力値が不正です")
        
    return P_C,P_C_len

def char_to_int(P_C: str)->int:

    P_C_list = list(P_C)#1文字ずつ格納。
    even_odd = len(P_C_list) % 2 #長さを入力
    
    if even_odd == 0 :#even    
        P_C_size = len(P_C_list) // 2
    else:#odd
        P_C_size = (len(P_C_list)+1) // 2
        P_C_list.append(" ")
        
    num_list = sp.zeros(2,P_C_size)
    #print(num_list)
    #入力
    box = 0
    for i in range(0,2):#行
        for j in range(0,P_C_size):#列 
            num_list[i,j] = ord(P_C_list[box])-32
            box += 1 #１個ずつ入力
            
    return num_list

def int_to_char(P_C: int,) ->chr: ##２次元配列→1次元配列+数字から文字 N=95
    P_C_size = len(P_C) // 2 #４個→[[1,2],[3,4]]半分の２個に
    
    char_list = []#数字を文字にする
    box = 0#２次元配列→1次元配列
    for i in range(0,2):#2行だから
        for j in range(0,P_C_size): 
            char_list.append(chr(P_C[box]+32))#+32で元の文字に戻す。特殊文字を避けるため
            box += 1 #１個ずつ入力
    char_list = "".join(char_list)#"",""を結合する
    return char_list

def key(mod):
    try:
        A = sp.randMatrix(2,2,0,mod)
        A_inverse = A.inv_mod(mod)
    except sp.matrices.common.NonInvertibleMatrixError:
        A,A_inverse = key(mod)
    return A,A_inverse  

def key_P_C_insert():
    row = int(input("行row="))
    column = int(input("列column="))
    a = row * column
    A = sp.Matrix(row,column,range(a))
    print(F"A={A}")
    for i in range (row):#012
        for j in range (column):#01
            A[i,j] = int(input(F"{A[i,j]}\tA={i},{j}\n入力:")) 
    return A

if __name__ == "__main__":
    main()
   

