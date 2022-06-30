# Germail

صانع اميلات مؤقتة تستخدم خدمة من موقع mail.tm و تم عمل لها برنمج بسيط من خلال بايثون 
طريقة التثبيت هي 

## Install germail
امر التثبيت هو
```
pip3 install germail
```
## Import Germail
لما تنتهي من التثبيت يمكنك استدعاء المكتبة بكتابة كود  
```
import germail
```
## Create mail
سيظهر لك الاميل و كلمة السر بعد كتابة الكود هذا : 

```
user=germail.Germail()
```
## Show messages 
ستظهر لك جميع الرسائل بستخدام الكود التالي : 
```
messages=user.get_messages()
```
## Show last message
اظهار فقط اخر رسالة 
```
last=user.get_last_message()
```

## Show message by ID of message
اظهار الرسالة عن طريق id تبعها (ملاحظة يمكنك العثور على id من خلال اظهار جميع الرسائل ستظهر معها id ) 
```
msg=user.read_message("515454465414494ds444554")
```

## Login into other mail
يمكنك تسجيل الدخول الى اميل اخر تم صنعه من قبل من خلال الكود :
```
user.login("email@exmple.com","pasword")
```
## Delete mail or Renew email or Create other new Mail 
يمكنك حذف الاميل او تجديد الاميل او صنع اميل جديد من خلال هذي الاكواد التالية 
```
user.delete_account()
```
### or 
```
user.renew_account()
```
### or
```
user.new_account()
```


