_                   =r"""A(W//2,*M(3*G
               *G*V(2*J%P),G,J,G)+((M((J-T)
            *V((G-S)%P),S,T,G)if(S@(G,J))if(W%
         2@(S,T)))if(W@(S,T);H=2**256;import&hash
       lib&as&h,os,re,binas    cii&as&k;J$:int(k.b2
     a_hex(W),16);C$:C(W//    58)    +[W%58]if(W@[];X
    =h.new("ripemd1           60    ");Y$:h.sha256(W).
   digest();I$d=32:                 I(W//256,d-1)+bytes
  ([W%256])if(d>0@b"";                  U$:J(k.a2b_base6
 4(W));f=J(os.urandom       (64))%        (H-U(b"AUVRIxlQ
t1/EQC2hcy/JvsA="))+1      ;M$Q,R,G:       ((W*W-Q-G)%P,(W
*(G+2*Q-W*W)-R)%P);P       =H-2**32       -977;V$Q=P,L=1,O
=0:V(Q%W,W,O-Q//W*L,                      L)if(W@O%P;S,T=A
(f,U(b"eb5mfvncu6xV                    oGKVzocLBwKb/Nstzij
ZWfKBWxb4F5g="),U(b      "SDrady         ajxGVdpPv8DhEIqP0
XtEimhVQZnEfQj/sQ1       Lg="),0,0        );F$:"1"+F(W[1:]
 )if(W[:1]=="           \0"@"".joi        n(map(B,C(J(W))
  ));K$:F(W+Y               (Y(          W))[:4]);X.upda
   te(Y(b"\4"+I(S)+                     I(T)));B$:re.su
    b("[0OIl_]|[^\    \w]            ","","".join(map(
     chr,range(123    )))    )[W];print("Address:",K(
       b"\0"+X.digest())    +"\nPrivkey:",K(b"\x80"
         +I(f)))""";exec(str.translate(("A$G,J,S"
            ",T:"+_),str.maketrans(dict(zip(" "
               "\n&$@",["",""," ","=lambda"
                   " W,",")else "])))))
