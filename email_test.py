import gmail
#replace with your email_id & app_pass
email_id="pramodnainwal22@gmail.com"
app_pass="hvbj srab wkdb jyzi"

def send_openacn_ack(uemail,uname,uacn,upass):
    con=gmail.GMail(email_id,app_pass)
    sub="Congrats😊😄,Account opened successfully"

    utext="""Hello,{uname}
Welcome to ABC Bank
Your Acc NO is {uacn}
Your Pass is {upass}
Kindly change your password when you login first

Thanks
ABC Bank 
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp(uemail,otp,amt):
    con=gmail.GMail(email_id,app_pass)
    sub="OTP for fund transfer"

    utext=f"""your otp is {otp} to transfer amount {amt} 

Kindly use this otp to complete transfer
Please don't share to anyone else

Thanks
ABC Bank 
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)

def send_otp_4_pass(uemail,otp):
    con=gmail.GMail(email_id,app_pass)
    sub="OTP for password recovery"

    utext=f"""your otp is {otp} to recover password 

Kindly use this otp to complete transfer
Please don't share to anyone else

Thanks
ABC Bank 
Noida
    """
    msg=gmail.Message(to=uemail,subject=sub,text=utext)
    con.send(msg)
