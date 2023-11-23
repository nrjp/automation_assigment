from typing import Union
from fastapi import FastAPI
from selenium import webdriver
from pydantic import BaseModel
from selenium.webdriver.common.by import By
import time

app = FastAPI()


class FormFields(BaseModel):
    name: str                        # name
    email: str                       # email
    merek: str                       # Intellectual Property
    nomor_registrasi: int            # Registration Number
    nama_pemilik: str                # Owner Name    
    # pemilik_haki_:str              # I am the rights owner of the Intellectual Property
    hubungan_pelapor:str             # Informant's Relationship with the rights owner
    nama_perusahaan:str              # Informant's Company Name
    website_perusahaan:str           # Informant's Company Website
    alamat_perusahaan:str            # Informant's Company Address
    alamat_email_pemilik_merek:str   # Intellectual Property Owner’s or Informant’s Email
    no_telepon_pelapor:int           # Informant’s Phone Number
    link_barang:str                  # Link Produk (Product's Link)
    body:str                         # Detail Masalah (Problem Details)
    link_barang_banyak:str           # If you wish to report more than one product
    surat_kepemilikan_merek:str      # Proof of Intellectual Property Certificate)
    bukti_surat_kuasa:str            # The power of attorney from the owner of the Intellectual Property to the informant
    bukti_surat_izin_usaha:str       # Direct selling license


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/auto/")
async def fillform(FormFields:FormFields):
    driver = webdriver.Chrome()

    driver.get("https://bukabantuan.bukalapak.com/form/175")

    for input in FormFields:
        print(input)
        input_element = driver.find_element("name", input[0])
        input_element.send_keys(input[1])

    radio = driver.find_element(By.CLASS_NAME,'bl-radio-button__input')
    radio.click()
    driver.find_element(By.CLASS_NAME,'bl-checkbox').click()
    submit_button = driver.find_element(By.CLASS_NAME,"bl-button")
    submit_button.click()
    time.sleep(15)

    driver.quit()




