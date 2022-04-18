
"""

Örnek Uygulama 

Smtp Modülü ile Mail gönderme

"""

# secure connection oluşturmak için ya 'SMTP_SLL()' portno:465 veya '.starttls()' portno:587 kullanılabilir.
# SMTP_SSL() programın başlangıcında güvenli bir bağlantı oluşturur.
# starttls ise başlangıçta güvensiz olana ancak sizin '.starttls()' çağırmanızla güvenli hale gelen bir bağlantı oluşturur.

import smtplib
from email.mine.text import MIMEText  # Türkçe karakter için mimetext gerekli

try:
    # Gmail server adı ve portu yazarız
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Güvenlik ekliyoruz
    smtp.starttls()
    
    # Email adresimiz ve şifremiz
    smtp.login("Email adresiniz","password")
    
    # Gönderilecek mesaj
    mesaj = "Merhaba Python ile gönderdim"
    msg = MIMEText(mesaj.encode('utf-8'),_charset='utf-8') # Türkçe karakterler için
    
    
    # Gönderilecek hesaplar
    smtp.sendmail("Gönderen email", "Gönderilecek email", msg.as_string())
    #             sender_email_id           alıcı mail adresi
    
    # Bağlantıyı sonlandırırız
    smtp.quit()
    print("Email başarıyla gönderildi")
    
except Exception as ex:
    print("Birşeyler ters gitti email gönderilemedi...", ex)


