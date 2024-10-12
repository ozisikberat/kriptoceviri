import streamlit as st
import requests
import uuid
r= requests.get("https://api.coinlore.net/api/tickers/")
veri= r.json()
coinler=veri["data"]
coinfiyat={}
for coin in coinler:
  sembol=coin["symbol"]
  fiyat=coin["price_usd"]
  coinfiyat.update({sembol:float(fiyat)})
#print(coinfiyat)
coin_isimler=coinfiyat.keys()
coin1=st.sidebar.selectbox("eldeki coin",coin_isimler)
miktar=st.sidebar.number_input("miktar")
coin2=st.sidebar.selectbox("hedef coin",coin_isimler)
coinfiyat.get("CNX")
c1=coinfiyat.get(coin1)
c2=coinfiyat.get(coin2)
sonuc=c1*miktar/c2 # 20 CNX KAÇ BTC
st.write(miktar,"adet",coin1,sonuc,"adet",coin2)
st.link_button("satın almaya git",f"https://www.coinbase.com/tr/converter/{coin1}/{coin2}")
uuid.uuid4()


