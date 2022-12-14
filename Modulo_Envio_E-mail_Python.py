
# coding: utf-8

# In[288]:


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
#from tqdm import tqdm
from tqdm import tqdm_notebook as tqdm


# In[289]:


# create message object instance
msg = MIMEMultipart()

message = "Cacete"


# In[290]:


# Configuração dos parâmentros da mensagem
password = "SenhaEmailRemetente"
msg['From'] = "EmailRemetente"
msg['To'] = "EmailDestinatário"
msg['Subject'] = "AssuntoDoEmail"


# In[291]:


# add in the message body
msg.attach(MIMEText(message, 'plain'))


# In[292]:


# Criação do servidor de envio 
server = smtplib.SMTP('smtp.office365.com: 587')
server.starttls()


# In[293]:


# Login com usuário e senha 
server.login(msg['From'], password)
 


# In[294]:


#Envio do e-mail! Foi adicionando um barra de proguesso, porém não é necessário.

values = range(0,10)


with tqdm(total=len(values)) as pbar:
    for i in values:
        pbar.write('processed: %d' %i)
        pbar.update(1)
        sleep(1)
        if i == 9:
            # Envio pelo servidor smtp.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            #Encerrando a comunicação com o servidor
            server.quit()
            print("successfully sent email to %s:" % (msg['To']))
        else:
            print('Aguarde, seu e-mail será enviado quando o processo chegar no 9 %d' %i)

