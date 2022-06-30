# Germail
صانع اميلات مؤقتة تستخدم خدمة من موقع mail.tm و تم عمل لها برنمج بسيط من خلال بايثون 
طريقة التثبيت هي 
## install germail

```
pip3 install germail
```

لما تنتهي من التثبيت يمكنك استدعاء المكتبة بكتابة كود 
## import germail 
```
import germail
```
### create mail
سيظهر لك الاميل و كلمة السر بعد كتابة الكود هذا : 

```
user=germail.Germail()
```
### show messages 
ستظهر لك جميع الرسائل بستخدام الكود التالي : 
```
messages=user.get_messages()
```
### show last message
اظهار فقط اخر رسالة 
```
last=user.get_last_message()
```

### show message by id of message
اظهار الرسالة عن طريق id تبعها (ملاحظة يمكنك العثور على id من خلال اظهار جميع الرسائل ستظهر معها id ) 
```
msg=user.read_message("515454465414494ds444554")
```



